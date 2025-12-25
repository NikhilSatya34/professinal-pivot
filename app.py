import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Professional Pivot",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "started" not in st.session_state:
    st.session_state.started = False

# -------------------------------------------------
# INTRO PAGE
# -------------------------------------------------
if not st.session_state.started:

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <h1 style='text-align:center;'>🎓 Professional Pivot</h1>
    <h4 style='text-align:center; color:#94a3b8;'>
        Resume-driven Career Reality Check
    </h4>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    ### 🎯 Purpose of this Website
    **Professional Pivot** is not a normal job recommendation platform.

    - 📄 Resume is the **primary truth source**
    - 🧠 Skills are validated against **real job expectations**
    - ⚠️ Weak or mismatched profiles are **not comforted**
    - 🚀 Only realistic opportunities are shown
    - 🔍 Helps students understand **where they actually stand**
    """)

    st.info(
        "This honesty-driven platform prepares students for "
        "real industry standards instead of false hopes."
    )

    col = st.columns([1, 2, 1])[1]
    with col:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:#94a3b8;'>"
        "Project developed by <b>B. Nikhil Satya</b> – CSD<br>"
        "<b>25ALCSD002</b></p>",
        unsafe_allow_html=True
    )

# -------------------------------------------------
# MAIN APPLICATION
# -------------------------------------------------
else:

    # ---------------- HEADER ----------------
    c1, c2 = st.columns([1, 9])
    with c1:
        if st.button("⬅ Back"):
            st.session_state.started = False
            st.rerun()

    with c2:
        st.markdown("""
        <h1 style="margin-bottom:0;">🎓 Professional Pivot</h1>
        <p style="color:#94a3b8;">Resume &gt; Skills &gt; Reality</p>
        """, unsafe_allow_html=True)

    # ---------------- LOAD DATA ----------------
    @st.cache_data
    def load_data():
        return pd.read_csv("new1.csv")

    df = load_data()

    # ---------------- INPUT FLOW ----------------
    st.subheader("🔍 Student Profile")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        stream = st.selectbox("Stream", sorted(df["stream"].unique()))

    with c2:
        course = st.selectbox(
            "Course",
            sorted(df[df["stream"] == stream]["course"].unique())
        )

    with c3:
        department = st.selectbox(
            "Department",
            sorted(
                df[
                    (df["stream"] == stream) &
                    (df["course"] == course)
                ]["department"].unique()
            )
        )

    with c4:
        role = st.selectbox(
            "Job Role",
            sorted(
                df[
                    (df["stream"] == stream) &
                    (df["course"] == course) &
                    (df["department"] == department)
                ]["job_role"].unique()
            )
        )

    with c5:
        cgpa = st.slider("CGPA", 5.0, 10.0, 7.0, 0.1)

    resume = st.file_uploader(
        "📄 Upload Resume (Mandatory)",
        type=["txt", "pdf", "docx"]
    )

    submit = st.button("🔍 Validate Profile")

    # ---------------- RESULTS ----------------
    if submit:

        if not resume:
            st.warning("⚠️ Kindly Upload the Resume")
            st.stop()

        resume_text = resume.read().decode(errors="ignore").lower()

        all_skills = set(
            ",".join(df["required_skill"].dropna()).lower().split(",")
        )
        user_skills = [s.strip() for s in all_skills if s.strip() in resume_text]

        base = df[
            (df["stream"] == stream) &
            (df["course"] == course) &
            (df["department"] == department) &
            (df["job_role"] == role)
        ]

        st.subheader("📊 Career Reality Check")

        cols = st.columns(2)
        shown = False

        for i, (_, row) in enumerate(base.iterrows()):

            required = [s.strip().lower() for s in row["required_skill"].split(",")]

            matched = set(required) & set(user_skills)
            missing = set(required) - set(user_skills)

            match_percent = int((len(matched) / len(required)) * 100) if required else 0

            # Readiness label
            if match_percent <= 30:
                readiness = "❌ Not Ready"
                prep = "4–6 months"
            elif match_percent <= 60:
                readiness = "⚠️ Partially Ready"
                prep = "2–3 months"
            elif match_percent <= 80:
                readiness = "✅ Near Ready"
                prep = "1–2 months"
            else:
                readiness = "🚀 Job Ready"
                prep = "0–1 month"

            shown = True

            # Skill display with ✔ ❌
            skills_html = ""
            for skill in required:
                if skill in matched:
                    skills_html += f"<span style='color:#22c55e;'>✔ {skill}</span> &nbsp; "
                else:
                    skills_html += f"<span style='color:#ef4444;'>❌ {skill}</span> &nbsp; "

            with cols[i % 2]:
                st.markdown(f"""
                <div style="
                    background:#020617;
                    padding:18px;
                    border-radius:16px;
                    margin-bottom:20px;
                    box-shadow:0 14px 35px rgba(0,0,0,0.6);
                ">
                    <h4>🏢 {row['company_name']}</h4>
                    <p>📍 {row['location']} | <b>{row['company_level']}</b></p>

                    <p><b>Skill Match:</b> {match_percent}%</p>
                    <p><b>Readiness:</b> {readiness}</p>
                    <p><b>Missing Skills:</b> {len(missing)} / {len(required)}</p>
                    <p><b>Estimated Prep Time:</b> {prep}</p>

                    <hr style="border:0.5px solid #1e293b;">
                    <b>Required Skills</b><br>
                    {skills_html}

                    <hr style="border:0.5px solid #1e293b;">
                    <b>Why shown?</b>
                    <ul>
                        <li>Matches selected role</li>
                        <li>Resume skills evaluated</li>
                        <li>CGPA eligible</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

        if not shown:
            st.warning(
                "⚠️ Your resume skills do not align with the selected job role. "
                "Please improve your skills or update your resume."
            )
