from src.heuristic import euclidean_distance, manhattan_distance

start = (0, 0)
goal = (2, 1)

euc_dist = euclidean_distance(start, goal)
man_dist = manhattan_distance(start, goal)

print("Euclidean Distance:", euc_dist)
print("Manhattan Distance:", euc_dist)

"""
Notice:
Running `python .\\tests\\manual\\heuristic.py` Gives Error of ModuleNotFoundError

------------------

From Root Directory
Run: `python -m tests.manual.heuristic`
"""
