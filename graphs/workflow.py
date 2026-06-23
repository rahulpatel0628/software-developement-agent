from langgraph.graph import StateGraph, START, END
from state.state import SoftwareState
from agents.team_lead import team_lead_node
from agents.backend import backend_node
from agents.reveiwer import reviewer_node
from agents.backend_planner import backend_planner_node
from agents.tester import tester_node

def review_router(state: SoftwareState):
    score = state.get("review_report",{}).get("score",0)

    iterations = state.get("review_iterations",0)

    if score >= 8:
        return "end"

    if iterations >= 3:
        return "end"

    return "backend"

def test_router(state: SoftwareState):

    testing_report = state.get("testing_report",{})

    score = testing_report.get("score",0)

    iterations = state.get("test_iterations",0)

    print(f"\nTEST SCORE: {score}")

    print(f"TEST ITERATIONS: {iterations}")

    if score >= 80:
        print("\nTests Passed")
        return "end"

    if iterations >= 3:
        print("\nMax Iterations Reached")
        return "end"

    print("\nRegenerating Backend")

    return "backend"

def build_graph():
    graph = StateGraph(SoftwareState)

    graph.add_node("team_lead",team_lead_node)
    graph.add_node("backend",backend_node)
    graph.add_node("reviewer",reviewer_node)
    graph.add_node("tester",tester_node)
   

    graph.add_edge(START,"team_lead")
    graph.add_edge("team_lead","backend")
    graph.add_edge("backend","reviewer")
    graph.add_edge("reviewer","tester")
    graph.add_conditional_edges("tester",test_router,{"backend": "backend","end": END})
    

    return graph.compile()