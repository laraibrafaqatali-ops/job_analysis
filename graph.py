from langgraph.graph import StateGraph, START, END
from models import GraphState
from nodes import (extraction_node, classification_node,
                   skill_analysis_node, report_node)

MIN_LENGTH = 30


def build_graph():
    g = StateGraph(GraphState)
    g.add_node("extraction", extraction_node)
    g.add_node("classification", classification_node)
    g.add_node("skill_analysis", skill_analysis_node)
    g.add_node("report", report_node)

    g.add_edge(START, "extraction")
    g.add_edge("extraction", "classification")
    g.add_edge("classification", "skill_analysis")
    g.add_edge("skill_analysis", "report")
    g.add_edge("report", END)
    return g.compile()


def validate_input(text: str):
    """Returns error message, or None if input is OK."""
    if not text or not text.strip():
        return "Job description khali hai. Please text paste karein."
    if len(text.strip()) < MIN_LENGTH:
        return "Job description bohat chhoti hai. Poori JD paste karein."
    return None


def run_analysis(job_description: str) -> dict:
    """Runs the graph. Returns {'report': {...}} or {'error': '...'}"""
    err = validate_input(job_description)
    if err:
        return {"error": err}
    try:
        app = build_graph()
        final_state = app.invoke({"job_description": job_description.strip()})
        return {"report": final_state["report"]}
    except Exception as e:
        return {"error": f"Analysis fail ho gaya: {e}"}