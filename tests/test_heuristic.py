from src.heuristic import euclidean_distance, manhattan_distance

start = (0, 0)
goal = (2, 1)

euc_dist = euclidean_distance(start, goal)
man_dist = manhattan_distance(start, goal)

print("Euclidean Distance:", euc_dist)
print("Manhattan Distance:", euc_dist)

"""
Running: `python .\tests\test_heuristic.py` Gives Error of ModuleNotFoundError. For Correction, Changed The Import Path Of graph_loader.py
And city_graph.json

------------------

From The Root Directory
Run: `python -m tests.test_heuristic`
Test: `python -m pytest`
"""
