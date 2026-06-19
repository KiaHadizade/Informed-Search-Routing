"""
Algorithm Comparison

Objective: A* VS IDA*

Based on:

Path Cost
Number of Visited Nodes
Execution Time
"""

import time
from src.astar import astar
from src.idastar import idastar

# Comparison Function
def compare_algorithms(graph, start, goal):
    # A* Executaion
    astar_start = time.perf_counter()
    astar_path, astar_cost, astar_visited = astar(graph, start, goal)
    astar_end = time.perf_counter()

    # Execution Time
    astar_time = (astar_end - astar_start)

    # IDA* Executaion
    idastar_start = time.perf_counter()
    idastar_path, idastar_cost, idastar_visited = idastar(graph, start, goal)
    idastar_end = time.perf_counter()

    # Execution Time
    idastar_time = (idastar_end - idastar_start)

    # Print The Results
    print("\n")
    print("=" * 50)
    print("               ALGORITHM COMPARISON")
    print("=" * 50)

    print(
        f"{'Algorithm':<15}"
        f"{'Cost':<10}"
        f"{'Visited':<12}"
        f"{'Time(s)':<12}"
    )

    print("-" * 50)

    print(
        f"{'A*':<15}"
        f"{astar_cost:<10}"
        f"{astar_visited:<12}"
        f"{astar_time:<12.8f}"
    )

    print(
        f"{'IDA*':<15}"
        f"{idastar_cost:<10}"
        f"{idastar_visited:<12}"
        f"{idastar_time:<12.8f}"
    )