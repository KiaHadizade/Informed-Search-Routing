from src.graph_loader import load_graph
from src.astar import astar
from src.idastar import idastar

def run():
    graph = load_graph("data/city_graph.json")

    start = (0, 0)
    goal = (2, 1)

    astar_path, astar_cost, _ = astar(graph, start, goal)
    idastar_path, idastar_cost, _ = idastar(graph, start, goal)

    assert astar_cost == idastar_cost

    print("[PASS] Correctness Test")
