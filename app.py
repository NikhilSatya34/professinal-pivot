import streamlit as st
import pandas as pd
import PyPDF2
import docx

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
# RESUME TEXT EXTRACTOR (PDF / DOCX / TXT)
# -------------------------------------------------
def extract_resume_text(file):
    text = ""

    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + " "

    else:  # TXT
        text = file.read().decode(errors="ignore")

    return text.lower()

# -------------------------------------------------
# INTRO PAGE
# -------------------------------------------------
if not st.session_state.started:

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>🎓 Professional Pivot</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align:center;color:#94a3b8;'>Resume → Skills → Reality</h4>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.write(
        "**Professional Pivot** is not a normal job recommendation website. "
        "It validates whether a student is actually ready for a selected role "
        "by strictly analyzing resume skills against real industry requirements."
    )

    st.info(
        "⚠️ This platform is intentionally strict. "
        "It shows reality, not false motivation."
    )

    if st.button("🚀 Get Started"):
        st.session_state.started = True
        st.rerun()

    st.markdown(
        "<p style='text-align:center;color:#94a3b8;'>"
        "Project developed by <b>B. Nikhil Satya</b> – CSD | <b>25ALCSD002</b>"
        "</p>",
        unsafe_allow_html=True
    )

# -------------------------------------------------
# MAIN APP
# -------------------------------------------------
else:

    # ---------------- BACK BUTTON + HEADER ----------------
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
        job_role = st.selectbox(
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
        type=["pdf", "docx", "txt"]
    )

    submit = st.button("🔍 Validate Profile")

    # ---------------- RESULTS ----------------
    if submit:

        if not resume:
            st.warning("⚠️ Kindly Upload the Resume")
            st.stop()

        resume_text = extract_resume_text(resume)

        # User skills from resume
        all_skills = set(
            ",".join(df["required_skill"].dropna())
            .lower()
            .replace("/", ",")
            .split(",")
        )
        user_skills = {s.strip() for s in all_skills if s.strip() and s in resume_text}

        base = df[
            (df["stream"] == stream) &
            (df["course"] == course) &
            (df["department"] == department) &
            (df["job_role"] == job_role)
        ]

        st.subheader("📊 Career Reality Check")

        cols = st.columns(2)
        shown = False

        for i, (_, row) in enumerate(base.iterrows()):
            required = [s.strip().lower() for s in row["required_skill"].split(",")]

            matched = [s for s in required if s in user_skills]
            missing = [s for s in required if s not in user_skills]

            match_percent = int((len(matched) / len(required)) * 100) if required else 0

            shown = True

            # Readiness label
            if match_percent >= 80:
                readiness = "🚀 Job Ready"
            elif match_percent >= 50:
                readiness = "⚠️ Partially Ready"
            else:
                readiness = "❌ Not Ready"

            with cols[i % 2]:
                st.markdown(f"""
                <div style="
                    background:#020617;
                    padding:18px;
                    border-radius:18px;
                    margin-bottom:20px;
                    box-shadow:0 15px 35px rgba(0,0,0,0.6);
                    color:#e5e7eb;
                ">
                    <h4>🏢 {row['company_name']}</h4>
                    <p>📍 {row['location']} | <b>{row['company_level']}</b></p>

                    <p><b>Skill Match:</b> {match_percent}%</p>
                    <p><b>Readiness:</b> {readiness}</p>

                    <b>Required Skills</b><br>
                    {"".join(
                        f"<span style='background:#1e293b;padding:6px 12px;border-radius:999px;margin:4px;display:inline-block;'>"
                        f"<span style='color:#22c55e;'>✔</span> {s}</span>"
                        for s in matched
                    )}
                    {"".join(
                        f"<span style='background:#1e293b;padding:6px 12px;border-radius:999px;margin:4px;display:inline-block;'>"
                        f"<span style='color:#ef4444;'>❌</span> {s}</span>"
                        for s in missing
                    )}

                    <p style="margin-top:10px;color:#94a3b8;">
                        Missing Skills: {len(missing)} / {len(required)}
                    </p>
                </div>
                """, unsafe_allow_html=True)

        if not shown:
            st.warning(
                "⚠️ Your resume skills do not match the selected stream / course / role."
            )
