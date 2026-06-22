from src.graph_loader import load_graph
from src.astar import astar
from src.idastar import idastar

def test_algorithms_return_same_cost():
    graph = load_graph("data/city_graph.json")

    start = (0, 0)
    goal = (2, 1)

    _, astar_cost, _ = astar(graph, start, goal)
    _, idastar_cost, _ = idastar(graph, start, goal)

    assert astar_cost == idastar_cost

"""
From Root Directory
Run: `python -m pytest`
Or:  `python -m pytest -v`
"""
