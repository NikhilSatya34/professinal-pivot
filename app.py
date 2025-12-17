import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Career Readiness", layout="wide")

st.markdown("""
<style>
.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.45);
    transition: 0.3s ease;
}
.card:hover {
    transform: translateY(-6px);
}
.badge {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    color: white;
    margin-right: 6px;
}
.logo {
    width: 52px;
    height: 52px;
    background: white;
    padding: 6px;
    border-radius: 12px;
}
.flex {
    display: flex;
    gap: 14px;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Career Readiness & Company Recommender")
st.caption("Smart recommendations with professional UI")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/Companies_CGPA.csv", encoding="utf-8")
st.success("Company data loaded successfully!")

# ---------------- FILTER UI ----------------
st.subheader("🔍 Find Suitable Companies")

c1, c2, c3 = st.columns(3)

with c1:
    stream = st.selectbox("Stream", sorted(df["stream"].unique()))
with c2:
    department = st.selectbox(
        "Department",
        sorted(df[df["stream"] == stream]["department"].unique())
    )
with c3:
    role = st.selectbox(
        "Job Role",
        sorted(df[
            (df["stream"] == stream) &
            (df["department"] == department)
        ]["job_role"].unique())
    )

base_df = df[
    (df["stream"] == stream) &
    (df["department"] == department)
]

# ---------------- SORT ORDER ----------------
level_order = ["High", "Mid", "Low", "Startup"]
base_df["company_level"] = pd.Categorical(
    base_df["company_level"],
    categories=level_order,
    ordered=True
)

# ---------------- BEST MATCHES (ALL LEVELS) ----------------
best_df = base_df[
    base_df["job_role"] == role
].sort_values("company_level")

# ---------------- ALTERNATE ROLES ----------------
alt_df = base_df[
    base_df["job_role"] != role
].sort_values("company_level")

# ---------------- CARD ----------------
def card(row, tag):
    colors = {
        "High": "#22c55e",
        "Mid": "#facc15",
        "Low": "#3b82f6",
        "Startup": "#a855f7"
    }

    st.markdown(f"""
    <div class="card">
        <div class="flex">
            <img src="https://logo.clearbit.com/{row['company_name'].replace(' ','').lower()}.com"
                 class="logo"
                 onerror="this.style.display='none'"/>
            <div>
                <h4 style="margin:0;">{row['company_name']}</h4>
                <div style="margin-top:6px;">
                    <span class="badge" style="background:{colors.get(row['company_level'])}">
                        {row['company_level']}
                    </span>
                    <span class="badge" style="background:#334155;">
                        {tag}
                    </span>
                </div>
                <p style="margin-top:8px;">📍 {row['location']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DISPLAY ----------------
if submit:
    st.markdown("## 🏢 Recommended Companies")

    if not best_df.empty:
        st.subheader("🎯 Best Matches (High → Startup)")
        cols = st.columns(2)
        for i, (_, r) in enumerate(best_df.drop_duplicates().iterrows()):
            with cols[i % 2]:
                card(r, "Best Match")

    if not alt_df.empty:
        st.subheader("🔁 Alternate Opportunities")
        cols = st.columns(2)
        for i, (_, r) in enumerate(alt_df.drop_duplicates().iterrows()):
            with cols[i % 2]:
                card(r, "Alternate Role")


st.markdown("---")
st.caption("🚀 Final Professional Career Recommender")
