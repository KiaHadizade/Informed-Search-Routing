# Informed Search Routing

Implementation of A* and IDA* algorithms for solving optimal pathfinding problems in weighted graph-based city maps.

---

## Project Overview

This project demonstrates how informed search algorithms can be used to find the least-cost route between two nodes in a weighted graph.

Implemented algorithms:

- A* Search
- IDA* Search (Iterative Deepening A*)

The graph represents a city map where:

- Nodes = intersections
- Edges = roads
- Edge weights = distance or travel cost

---

## Features

- Load graph from JSON file
- Run A* search
- Run IDA* search
- Compare algorithm performance
- Report visited nodes
- Report optimal path cost

---

## Project Structure

```text
Informed-Search-Routing/
│
├── data/
│   └── city_graph.json
│
├── src/
│   ├── astar.py
│   ├── graph_loader.py
│   ├── heuristic.py
│   ├── idastar.py
│   ├── main.py
│   └── utils.py
│
├── tests/
│   └── test_algorithms.py
│
├── .gitignore
├── Project.pdf
├── README.md
└── requirements.txt
```