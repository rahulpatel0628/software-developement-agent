from langgraph.graph import StateGraph, START, END
from state.state import SoftwareState
from agents.team_lead import team_lead_node
from agents.backend import backend_node
from agents.reveiwer import reviewer_node
from agents.backend_planner import backend_planner_node
from agents.tester import tester_node
from agents.frontend import frontend_node

def test_router(state: SoftwareState):

    report = state["testing_report"]

    iterations = state.get("test_iterations",0)

    backend_score = report.get("backend_score",0)

    frontend_score = report.get("frontend_score",0)

    if iterations > 3:
        return "end"

    if backend_score < 5:
        return "backend"

    elif frontend_score < 4:
        return "frontend"

    return "end"

def merge(state: SoftwareState):
    return {}

def build_graph():
    graph = StateGraph(SoftwareState)

    graph.add_node("team_lead",team_lead_node)
    graph.add_node("backend",backend_node)
    graph.add_node("reviewer",reviewer_node)
    graph.add_node("tester",tester_node)
    graph.add_node("frontend",frontend_node)
    graph.add_node("merge",merge)

    graph.add_edge(START,"team_lead")
    graph.add_edge("team_lead","backend")
    graph.add_edge("team_lead","frontend")

    graph.add_edge("backend","merge")
    graph.add_edge("frontend","merge")

    graph.add_edge("merge","reviewer")

    graph.add_edge("reviewer","tester")
    graph.add_conditional_edges("tester",test_router,{"backend": "backend",
                                                      "frontend": "frontend",
                                                      "end": END
                                                      }
                                )
    

    return graph.compile()