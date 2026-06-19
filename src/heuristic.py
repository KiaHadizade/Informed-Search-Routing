import math

def euclidean_distance(node, goal):
    """
    Calculate Euclidean distance between two nodes

    Args:
        node: tuple (x, y)
        goal: tuple (x, y)

    Returns:
        float
    """

    x1, y1 = node
    x2, y2 = goal

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

def manhattan_distance(node, goal):

    x1, y1 = node
    x2, y2 = goal

    return abs(x2 - x1) + abs(y2 - y1)
