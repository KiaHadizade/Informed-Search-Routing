from src.idastar import idastar

def test_start_equals_goal():
    graph = {
        (0, 0): []
    }

    path, cost, _ = idastar(graph, (0, 0), (0, 0))

    assert path == [(0, 0)]
    assert cost == 0

def test_disconnected_graph():
    graph = {

        (0, 0): [
            ((1, 0), 1)
        ],

        (1, 0): [
            ((0, 0), 1)
        ],

        (5, 5): []
    }

    path, cost, _ = idastar(graph, (0, 0), (5, 5))

    assert path is None
    assert cost == float("inf")

"""
From Root Directory
Run: `python -m pytest`
Or:  `python -m pytest -v`
"""
