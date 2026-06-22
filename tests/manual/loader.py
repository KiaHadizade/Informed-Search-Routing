from src.graph_loader import load_graph

graph = load_graph("data/city_graph.json")
for node, neighbors in graph.items():
    print(node, "->", neighbors)


"""
Notice:
Running `python .\\tests\\manual\\loader.py` Gives Error of ModuleNotFoundError

------------------

From Root Directory
Run: `python -m tests.manual.loader`
"""
