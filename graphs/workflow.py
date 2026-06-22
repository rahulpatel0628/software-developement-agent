from langgraph.graph import StateGraph, START, END
from state.state import SoftwareState
from agents.team_lead import team_lead_node


def build_graph():
    graph = StateGraph(SoftwareState)

    graph.add_node("team_lead",team_lead_node)
    
    graph.add_edge(START,"team_lead")

    graph.add_edge("team_lead",END)

    return graph.compile()