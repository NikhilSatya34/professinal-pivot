import streamlit as st
import pandas as pd
import pdfplumber
from docx import Document

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Career Readiness & Company Recommender",
    layout="wide"
)

st.markdown("""
<style>
.card {
    background: linear-gradient(135deg, #0f172a, #020617);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
    transition: all 0.3s ease;
    height: 100%;
}
.card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 18px 40px rgba(0,0,0,0.6);
}
.badge {
    display: inline-block;
    padding: 5px 14px;
    font-size: 12px;
    border-radius: 999px;
    color: white;
    margin-right: 6px;
}
.logo {
    width: 54px;
    height: 54px;
    background: white;
    padding: 6px;
    border-radius: 12px;
    margin-right: 12px;
}
.row-flex {
    display: flex;
    align-items: center;
    gap: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Career Readiness & Company Recommender")
st.caption("Professional career recommendations based on stream, role, CGPA & resume skills")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("data/Companies_CGPA.csv", encoding="utf-8")

df = load_data()
st.success("Company data loaded successfully!")

# ---------------- LOGO HELPER ----------------
def get_company_logo(company_name):
    domain_map = {
        "tcs": "tcs.com",
        "infosys": "infosys.com",
        "wipro": "wipro.com",
        "accenture": "accenture.com",
        "cognizant": "cognizant.com",
        "capgemini": "capgemini.com",
        "ibm": "ibm.com",
        "amazon": "amazon.com",
        "microsoft": "microsoft.com",
        "google": "google.com",
        "deloitte": "deloitte.com"
    }
    name = company_name.lower()
    for key in domain_map:
        if key in name:
            return f"https://logo.clearbit.com/{domain_map[key]}"
    return f"https://logo.clearbit.com/{name.replace(' ', '')}.com"

# ---------------- FILTER UI ----------------
st.subheader("🔍 Find Suitable Companies")

col1, col2, col3 = st.columns(3)

with col1:
    stream = st.selectbox("Stream", sorted(df["stream"].dropna().unique()))

with col2:
    department = st.selectbox(
        "Department",
        sorted(df[df["stream"] == stream]["department"].dropna().unique())
    )

with col3:
    role = st.selectbox(
        "Job Role",
        sorted(df[
            (df["stream"] == stream) &
            (df["department"] == department)
        ]["job_role"].dropna().unique())
    )

cgpa = st.slider("Your CGPA", 5.0, 10.0, 7.0, 0.1)

def cgpa_level(c):
    if c >= 8.0:
        return "High"
    elif c >= 6.5:
        return "Mid"
    else:
        return "Low"

level = cgpa_level(cgpa)

base_df = df[
    (df["stream"] == stream) &
    (df["department"] == department)
]

primary_df = base_df[
    (base_df["job_role"] == role) &
    (base_df["company_level"].str.lower() == level.lower())
]

alternate_df = base_df[
    (base_df["job_role"] != role) &
    (base_df["company_level"].str.lower() == level.lower())
]

# ---------------- CARD RENDER ----------------
def render_card(row, tag):
    colors = {
        "High": "#16a34a",
        "Mid": "#f59e0b",
        "Low": "#2563eb",
        "Startup": "#7c3aed"
    }
    color = colors.get(row["company_level"], "#64748b")
    logo = get_company_logo(row["company_name"])

    st.markdown(f"""
    <div class="card">
        <div class="row-flex">
            <img src="{logo}" class="logo" onerror="this.style.display='none'"/>
            <div>
                <h4 style="margin:0;">{row["company_name"]}</h4>
                <div style="margin-top:6px;">
                    <span class="badge" style="background:{color};">
                        {row["company_level"]}
                    </span>
                    <span class="badge" style="background:#334155;">
                        {tag}
                    </span>
                </div>
                <p style="margin-top:8px;opacity:0.85;">📍 {row["location"]}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DISPLAY ----------------
st.markdown("## 🏢 Recommended Companies")

if primary_df.empty and alternate_df.empty:
    st.info("No companies found. Try changing CGPA or role.")
else:
    if not primary_df.empty:
        st.subheader("🎯 Best Matches")
        cols = st.columns(2)
        for i, (_, row) in enumerate(primary_df.drop_duplicates().iterrows()):
            with cols[i % 2]:
                render_card(row, "Best Match")

    if not alternate_df.empty:
        st.subheader("🔁 Alternate Opportunities")
        cols = st.columns(2)
        for i, (_, row) in enumerate(alternate_df.drop_duplicates().iterrows()):
            with cols[i % 2]:
                render_card(row, "Alternate Role")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | Premium UI Career Recommendation System")
