from src.graph_loader import load_graph
from src.idastar import idastar

graph = load_graph("data/city_graph.json")

start = (0, 0)
goal = (2, 1)
path, cost, visited = idastar(graph, start, goal)

print("Path:", path)
print("Cost:", cost)
print("Visited Nodes:", visited)


"""
Notice:
Running `python .\\tests\\manual\\idastar.py` Gives Error of ModuleNotFoundError

------------------

From Root Directory
Run: `python -m tests.manual.idastar`
"""
