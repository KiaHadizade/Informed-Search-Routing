import os
from src.graph_loader import load_graph
from src.idastar import idastar

json_path = os.path.join(
    os.path.dirname(__file__), "../data/city_graph.json"
)
graph = load_graph(json_path)

start = (0, 0)
goal = (2, 1)
path, cost, visited = idastar(graph, start, goal)

print("Path:", path)
print("Cost:", cost)
print("Visited Nodes:", visited)

"""
Running: `python .\tests\test_idastar.py` Gives Error of ModuleNotFoundError. For Correction, Changed The Import Path Of graph_loader.py
And city_graph.json

------------------

From The Root Directory
Run: `python -m tests.test_idastar`
Test: `python -m pytest`
"""