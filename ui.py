import json
import streamlit as st
from graph import run_analysis

st.set_page_config(page_title="AI Job Description Analyzer", page_icon="📄")
st.title("📄 AI Job Description Analyzer")

jd = st.text_area("Job Description paste karein", height=250)


def tags(items, color):
    html = "".join(
        f"<span style='background:{color};color:white;padding:4px 12px;"
        f"border-radius:14px;margin:3px;display:inline-block;font-size:14px'>{i}</span>"
        for i in items
    )
    st.markdown(html, unsafe_allow_html=True)


if st.button("Analyze", type="primary"):
    with st.spinner("Analyzing..."):
        result = run_analysis(jd)

    if "error" in result:
        st.error(result["error"])
    else:
        r = result["report"]
        st.subheader("Structured Hiring Report")

        c1, c2 = st.columns(2)
        c1.metric("Job Title", r["job_title"])
        c2.metric("Company", r["company"])
        c3, c4, c5 = st.columns(3)
        c3.metric("Experience", r["experience"])
        c4.metric("Category", r["job_category"])
        c5.metric("Type", r["employment_type"])

        st.markdown("**Required Skills**")
        tags(r["required_skills"], "#4b6cb7")
        st.markdown("**Technical Skills**")
        tags(r["technical_skills"], "#1f8a70")
        st.markdown("**Soft Skills**")
        tags(r["soft_skills"], "#d97706")

        st.markdown("**Top 3 Skills**")
        for i, s in enumerate(r["top_3_skills"], 1):
            st.write(f"{i}. {s}")

        st.download_button(
            "⬇️ Download JSON",
            data=json.dumps(r, indent=2, ensure_ascii=False),
            file_name="hiring_report.json",
            mime="application/json",
        )