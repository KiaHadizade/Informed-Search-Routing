from src.graph_loader import load_graph

def test_graph_loads():
    graph = load_graph("data/city_graph.json")

    assert graph is not None
    assert len(graph) > 0

"""
From Root Directory
Run: `python -m pytest`
Or:  `python -m pytest -v`
"""
