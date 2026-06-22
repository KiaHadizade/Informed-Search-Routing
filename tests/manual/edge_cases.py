import time
from src.astar import astar
from src.idastar import idastar

def run():
    # Start == Goal
    graph = {
        (0, 0): []
    }

    path, cost, _ = astar(graph, (0, 0), (0, 0))

    assert path == [(0, 0)]
    assert cost == 0

    path, cost, _ = idastar(graph, (0, 0), (0, 0))

    assert path == [(0, 0)]
    assert cost == 0

    print("[PASS] Start Equals Goal")

    time.sleep(1)

    # Disconnected Graph
    graph = {
        (0, 0): [
            ((1, 0), 1)
        ],

        (1, 0): [
            ((0, 0), 1)
        ],

        (5, 5): []
    }

    path, cost, _ = astar(graph, (0, 0), (5, 5))

    assert path is None
    assert cost == float("inf")

    path, cost, _ = idastar(graph, (0, 0), (5, 5))

    assert path is None
    assert cost == float("inf")

    print("[PASS] Disconnected Graph")
