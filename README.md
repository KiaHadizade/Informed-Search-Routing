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
├── docs/
│   ├── Project.pdf
│   └── report.ipynb
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
│   ├── test_algorithms.py
│   └── test_loader.py
│
├── .gitignore
├── README.md
└── requirements.txt
```
## Install Dependencies
`pip install -r requirements.txt`

## References
[A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
[A* Search Algorithm](https://www.geeksforgeeks.org/dsa/a-search-algorithm/)
[Introduction to A*](https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html)
[A* Search Algorithm](https://viblo.asia/p/a-search-algorithm-aWj53BN1l6m)
[A* Algorithm (OCR A Level Computer Science): Revision Note](https://www.savemyexams.com/a-level/computer-science/ocr/17/revision-notes/8-algorithms/8-1-algorithms/a-algorithm/)
[Application of A* algorithm in intelligent vehicle path planning](https://www.extrica.com/article/22828)
[Introduction to the A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
[Amit’s A* Pages](https://theory.stanford.edu/~amitp/GameProgramming/)