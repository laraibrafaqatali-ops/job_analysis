from llm import get_llm
from models import (ExtractedInfo, Classification, SkillAnalysis,
                    HiringReport, GraphState)


def extraction_node(state: GraphState) -> GraphState:
    """Node 1: Information Extraction"""
    llm = get_llm().with_structured_output(ExtractedInfo)
    prompt = f"""Extract the job title, company name (if available),
required experience and required skills from this job description.

Job Description:
{state['job_description']}"""
    result = llm.invoke(prompt)
    return {"extracted": result.model_dump()}


def classification_node(state: GraphState) -> GraphState:
    """Node 2: Job Classification"""
    llm = get_llm().with_structured_output(Classification)
    prompt = f"""Classify this job.
Job category: AI, Web Development, Data Science, Mobile, etc.
Employment type: Full-time, Part-time, Internship, Remote, Hybrid or On-site.

Job Description:
{state['job_description']}"""
    result = llm.invoke(prompt)
    return {"classification": result.model_dump()}


def skill_analysis_node(state: GraphState) -> GraphState:
    """Node 3: Skill Analysis"""
    llm = get_llm().with_structured_output(SkillAnalysis)
    prompt = f"""Based on the job info below, separate technical skills and
soft skills, and pick the top 3 most important skills.

Job Title: {state['extracted']['job_title']}
Required Skills: {state['extracted']['required_skills']}

Full Job Description:
{state['job_description']}"""
    result = llm.invoke(prompt)
    return {"skills": result.model_dump()}


def report_node(state: GraphState) -> GraphState:
    """Node 4: Hiring Report"""
    e, c, s = state["extracted"], state["classification"], state["skills"]
    report = HiringReport(
        job_title=e["job_title"],
        company=e["company_name"] or "Not specified",
        experience=e["required_experience"],
        required_skills=e["required_skills"],
        job_category=c["job_category"],
        employment_type=c["employment_type"],
        technical_skills=s["technical_skills"],
        soft_skills=s["soft_skills"],
        top_3_skills=s["top_3_skills"][:3],
    )
    return {"report": report.model_dump()}

