# ===== Impoprt Libraries =====
import heapq # Needed For Priority Queue
from src.heuristic import euclidean_distance

# ===== Path Reconstruction Function =====
def reconstruct_path(came_from, current):

    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path

# ===== A* Function Skeleton =====
def astar(graph, start, goal):

    # ===== Definition Of Open Set =====
    # Priority Queue maintains: (f_score, node)
    open_set = []
    heapq.heappush(
        open_set,
        (0, start)
    )

    # ===== Building Data Structures =====
    # Parents
    came_from = {}

    # Actual Cost
    g_score = { start: 0 }

    # Estimated Cost
    f_score = {
        start: euclidean_distance(start, goal)
    }

    # Number of visits
    visited_nodes = 0
    closed_set = set()

    # ===== Main Loop =====
    while open_set:
        # Get The Best Node
        current_f, current = heapq.heappop(open_set)
        # To Avoid Duplicate Visits
        if current in closed_set:
            continue

        closed_set.add(current)
        visited_nodes += 1

        # ===== Check The Target =====
        if current == goal:
            path = reconstruct_path(came_from, current)

            return (
                path,
                g_score[current],
                visited_nodes
            )

        # ===== Check Neighbors =====
        for neighbor, cost in graph[current]:
            # New Cost Calculation
            tentative_g = (g_score[current] + cost)

            # ===== If A Better Path Is Found =====
            if (neighbor not in g_score or tentative_g < g_score[neighbor]):
                # Save Parent
                came_from[neighbor] = current

                # Save g
                g_score[neighbor] = tentative_g

                # h Calculation
                h = euclidean_distance(neighbor, goal)

                # f Calculation
                f = tentative_g + h
                f_score[neighbor] = f

                # Add To Queue
                heapq.heappush(
                    open_set,
                    (f, neighbor)
                )
    # If The Path Did Not Exist
    return None, float("inf"), visited_nodes
