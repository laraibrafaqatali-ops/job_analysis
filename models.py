from typing import List, Optional, TypedDict
from pydantic import BaseModel, Field


class ExtractedInfo(BaseModel):
    job_title: str = Field(description="Job title")
    company_name: Optional[str] = Field(default="Not specified", description="Company name if available")
    required_experience: str = Field(description="e.g. 2-4 Years")
    required_skills: List[str]


class Classification(BaseModel):
    job_category: str = Field(description="AI, Web Development, Data Science, Mobile, etc.")
    employment_type: str = Field(description="Full-time, Part-time, Internship, Remote, Hybrid, On-site")


class SkillAnalysis(BaseModel):
    technical_skills: List[str]
    soft_skills: List[str]
    top_3_skills: List[str] = Field(description="Exactly 3 most important skills")


class HiringReport(BaseModel):
    job_title: str
    company: str
    experience: str
    required_skills: List[str]
    job_category: str
    employment_type: str
    technical_skills: List[str]
    soft_skills: List[str]
    top_3_skills: List[str]


class GraphState(TypedDict, total=False):
    job_description: str
    extracted: dict
    classification: dict
    skills: dict
    report: dict
    error: str