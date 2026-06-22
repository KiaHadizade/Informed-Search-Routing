from src.graph_loader import load_graph
from src.comparison import compare_algorithms

graph = load_graph("data/city_graph.json")

compare_algorithms(graph, (0, 0), (2, 1))

"""
Notice:
Running `python .\\tests\\manual\\comparison.py` Gives Error of ModuleNotFoundError

------------------

From Root Directory
Run: `python -m tests.manual.comparison`
"""
