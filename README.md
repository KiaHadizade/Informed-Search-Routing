# Informed Search Routing

Implementation of A* and IDA* informed search algorithms for optimal pathfinding in weighted graph

---

## Project Overview

This project solves a routing problem in a weighted graph representing a city map. The goal is to find the least-cost path between a start node and a goal node using informed search algorithms

Implemented algorithms:

- A* Search
- IDA* Search (Iterative Deepening A*)

Graph Model:

- Nodes represent intersections
- Edges represent roads
- Edge weights represent travel cost (distance or time)

Example:

```
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1.5)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)]
}
```

---

## Heuristic

Euclidean Distance:

`h(n) = sqrt((x2 - x1)^2 + (y2 - y1)^2)`

or

Manhattan Distance:

`h(n) = |x2 - x1| + |y2 - y1|`

---

## Features

- Load graph from JSON file
- A* pathfinding
- IDA* pathfinding
- Algorithm comparison
- Visited node statistics
- Command-line interface
- Automated tests

---

## Project Structure

```
Informed-Search-Routing/
│
├── data/
│   └── city_graph.json
│
├── docs/
│   ├── img/
│   ├── Project.pdf
│   └── report.ipynb
│
├── src/
│   ├── astar.py
│   ├── comparison.py
│   ├── graph_loader.py
│   ├── heuristic.py
│   ├── idastar.py
│   └── main.py
│
├── tests/
│   ├── manual/
│   │    ├── astar.py
│   │    ├── basic.py
│   │    ├── comparison.py
│   │    ├── correctness.py
│   │    ├── edge_cases.py
│   │    ├── heuristic.py
│   │    ├── idastar.py
│   │    ├── loader.py
│   │    └── run_tests.py
│   │
│   ├── pytest/
│   │    ├── test_astar.py
│   │    ├── test_correctness.py
│   │    ├── test_idastar.py
│   │    └── test_loader.py
│   └── test.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Install Dependencies

`pip install -r requirements.txt`

---

## Run

`python src/main.py`

---

## Example Output

Path:
[(0,0), (0,1), (1,1), (2,1)]

Cost:
3.5

Visited Nodes:
6

---

> [!NOTE]
> Python Supports Implicit Namespace Packages (PEP 420), Which Means A Directory Can Be Treated As A Package Even Without An `__init__.py` That's Why We Are Using `python -m folderName.fileName` To Run Test Files

> [!NOTE]
> To Disable Bytecode Generation, Run: `python -B -m folderName.fileName`
> Or Put Below Code At The Very Top Of The Script:
```
import sys
sys.dont_write_bytecode = True
```

> The Most Common Approach Is Ignoring It In Git:
```
__pycache__/
*.py[cod]
```

---
