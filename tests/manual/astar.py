from src.graph_loader import load_graph
from src.astar import astar

graph = load_graph("data/city_graph.json")

start = (0, 0)
goal = (2, 1)

path, cost, visited = astar(graph, start, goal)

print("Path:", path)
print("Cost:", cost)
print("Visited:", visited)

"""
Notice:
Running `python .\\tests\\manual\\astar.py` Gives Error of ModuleNotFoundError

------------------

From Root Directory
Run: `python -m tests.manual.astar`
"""
