# ===== Impoprt Libraries =====
from src.heuristic import euclidean_distance

def compute_cost(graph, path):
    """
    Calculate total cost of a path.
    """

    cost = 0
    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        for neighbor, edge_cost in graph[current]:
            if neighbor == next_node:
                cost += edge_cost
                break
    return cost

# SEARCH Recursive Function
def search(graph, node, goal, g, threshold, path, visited_nodes):
    """
    Recursive DFS used by IDA*
    Params:
    node => current node
    goal => goal
    g => actual cost
    threshold => current threshold
    path => current path
    visited_nodes => counter
    """

    # Calculate f
    visited_nodes[0] += 1
    f = g + euclidean_distance(node, goal)

    # Prune Branch
    if f > threshold:
        return f

    # Goal Found
    if node == goal:
        return "FOUND"

    # Finding The Smallest Passed Value
    minimum = float("inf")

    # Visit Neighbors
    for neighbor, cost in graph[node]:

        # Avoid Cycles (This Is The Equivalent Of closed_set In DFS)
        if neighbor in path:
            continue
        
        # Enter The Path
        path.append(neighbor)

        # Callback
        result = search(graph, neighbor, goal, g + cost, threshold, path, visited_nodes)

        # If The Path Is Found
        if result == "FOUND":
            return "FOUND"

        # Update Minimum
        if result < minimum:
            minimum = result

        # Backtrack
        path.pop()
    return minimum

# IDA* Main Function
def idastar(graph, start, goal):
    """
    IDA* algorithm

    Returns:
        path
        cost
        visited_nodes
    """

    # Initial Threshold
    threshold = euclidean_distance(start, goal)
    # Counter
    visited_nodes = [0]

    # Main Loop
    while True:
        # Initial Path
        path = [start]

        # Call SEARCH
        result = search(graph, start, goal, 0, threshold, path, visited_nodes)

        # If Found, We Will Calculate The Cost
        if result == "FOUND":
            # Uility Function
            total_cost = compute_cost(graph, path)

            return (
                path.copy(),
                total_cost,
                visited_nodes[0]
            )

        # If Not Found
        if result == float("inf"):
            return (None, float("inf"), visited_nodes[0])

        # Increase The Threshold
        threshold = result
