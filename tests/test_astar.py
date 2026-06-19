import os
from src.graph_loader import load_graph
from src.astar import astar

json_path = os.path.join(
    os.path.dirname(__file__), "../data/city_graph.json"
)
graph = load_graph(json_path)

start = (0, 0)
goal = (2, 1)

path, cost, visited = astar(graph, start, goal)

print("Path:", path)
print("Cost:", cost)
print("Visited:", visited)

"""
Running: `python .\tests\test_heuristic.py` Gives Error of ModuleNotFoundError. For Correction, Changed The Import Path Of graph_loader.py
And city_graph.json

------------------

From The Root Directory
Run: `python -m tests.test_astar`
Test: `python -m pytest`
"""