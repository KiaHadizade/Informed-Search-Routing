"""
Algorithm Comparison

Objective: A* VS IDA*

Based on:

Path Cost
Number of Visited Nodes
Execution Time
Memory Consumption
"""

import time
import tracemalloc
from src.astar import astar
from src.idastar import idastar

# Comparison Function
def compare_algorithms(graph, start, goal):
    # A* Executaion
    tracemalloc.start()
    astar_start = time.perf_counter()
    astar_path, astar_cost, astar_visited = astar(graph, start, goal)
    astar_elapced_time = (time.perf_counter() - astar_start) # Execution Time

    astar_current, astar_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # IDA* Executaion
    tracemalloc.start()
    idastar_start = time.perf_counter()
    idastar_path, idastar_cost, idastar_visited = idastar(graph, start, goal)
    idastar_elapced_time = (time.perf_counter() - idastar_start) # Execution Time

    idastar_current, idastar_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    astar_memory = astar_peak / 1024
    idastar_memory = idastar_peak / 1024

    # Print The Results
    print("\n")
    print("=" * 60)
    print("                    ALGORITHM COMPARISON")
    print("=" * 60)

    print(
        f"{'Algorithm':<15}"
        f"{'Cost':<10}"
        f"{'Visited':<12}"
        f"{'Time(s)':<12}"
        f"{'Memory(kb)':<12}"
    )

    print("-" * 60)

    print(
        f"{'A*':<15}"
        f"{astar_cost:<10}"
        f"{astar_visited:<10}"
        f"{astar_elapced_time:<16.8f}"
        f"{astar_memory:.2f}"
    )

    print(
        f"{'IDA*':<15}"
        f"{idastar_cost:<10}"
        f"{idastar_visited:<10}"
        f"{idastar_elapced_time:<16.8f}"
        f"{idastar_memory:.2f}"
    )