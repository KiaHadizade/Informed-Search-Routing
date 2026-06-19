import json

def parse_node(node_str):
    """
    Convert:
        '1,2'
    to:
        (1,2)
    """
    
    x, y = node_str.split(",")
    return (int(x), int(y))

# Graph Validation
def validate_graph(graph):
    if not graph:
        raise ValueError("Graph is empty")

    for node, neighbors in graph.items():
        if not isinstance(node, tuple):
            raise TypeError("Invalid node format")

        for neighbor, cost in neighbors:
            if cost < 0:
                raise ValueError("Negative edge costs are not allowed")

def load_graph(file_path):
    """
    Load graph from JSON file
    """

    with open(file_path, "r") as file:
        raw_graph = json.load(file)

    graph = {}

    for node, neighbors in raw_graph.items():
        parsed_node = parse_node(node)
        graph[parsed_node] = []

        for neighbor, cost in neighbors:
            parsed_neighbor = parse_node(neighbor)

            graph[parsed_node].append(
                (parsed_neighbor, float(cost))
            )

    validate_graph(graph)
    return graph
