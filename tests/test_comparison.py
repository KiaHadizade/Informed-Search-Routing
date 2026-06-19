import os
from src.graph_loader import load_graph
from src.comparison import compare_algorithms

json_path = os.path.join(
    os.path.dirname(__file__), "../data/city_graph.json"
)
graph = load_graph(json_path)

compare_algorithms(
    graph,
    (0, 0),
    (2, 1)
)

"""
Running: `python .\tests\test_comparison.py` Gives Error of ModuleNotFoundError. For Correction, Changed The Import Path Of graph_loader.py
And city_graph.json

------------------

From The Root Directory
Run: `python -m tests.test_comparison`
Test: `python -m pytest`
"""