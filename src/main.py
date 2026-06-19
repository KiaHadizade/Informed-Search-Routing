# Imports
import os
from src.graph_loader import load_graph
from src.astar import astar
from src.idastar import idastar
from src.comparison import compare_algorithms

# Menu Display Function
def show_menu():

    print("\n")
    print("=" * 40)
    print("ROUTE FINDER")
    print("=" * 40)

    print("1. Run A*")
    print("2. Run IDA*")
    print("3. Compare Algorithms")
    print("4. Exit")

# Get Coordinates
def get_node_input(message):
    node = input(message)
    x, y = node.split(",")

    return (int(x), int(y))

# Execute A*
def run_astar(graph):
    start = get_node_input("Start Node (x, y): ")
    goal = get_node_input("Goal Node (x, y): ")

    path, cost, visited = astar(graph, start, goal)

    print("\nRESULTS")
    print("Path:", path)
    print("Cost:", cost)
    print("Visited Nodes:", visited)

# Execute IDA*
def run_idastar(graph):
    start = get_node_input("Start Node (x, y): ")
    goal = get_node_input("Goal Node (x, y): ")

    path, cost, visited = idastar(graph, start, goal)

    print("\nRESULTS")
    print("Path:", path)
    print("Cost:", cost)
    print("Visited Nodes:", visited)

# Main Function
def main():
    # Load Graph
    json_path = os.path.join(
        os.path.dirname(__file__), "../data/city_graph.json"
    )
    graph = load_graph(json_path)
    # graph = load_graph("../data/city_graph.json")

    # Application Loop
    while True:
        show_menu()
        choice = input("\nSelect Option: ")

        if choice == "1":
            run_astar(graph)

        elif choice == "2":
            run_idastar(graph)

        elif choice == "3":
            start = get_node_input("Start Node (x, y): ")
            goal = get_node_input("Goal Node (x, y): ")

            compare_algorithms(graph, start, goal)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid Option")

# Run The Program
if __name__ == "__main__":
    main()

"""
Running: `python .\\src\\main.py` Gives Error of ModuleNotFoundError

------------------

From The Root Directory
Run: `python -m src.main`
Test: `python -m pytest`
"""
