from langgraph.graph import StateGraph, START, END
from state.state import SoftwareState
from agents.team_lead import team_lead_node
from agents.backend import backend_node
from agents.reveiwer import reviewer_node

def build_graph():
    graph = StateGraph(SoftwareState)

    graph.add_node("team_lead",team_lead_node)
    graph.add_node("backend",backend_node)
    graph.add_node("reviewer",reviewer_node)

    graph.add_edge(START,"team_lead")
    graph.add_edge("team_lead","backend")
    graph.add_edge("backend","reviewer")
    graph.add_edge("reviewer",END)

    return graph.compile()