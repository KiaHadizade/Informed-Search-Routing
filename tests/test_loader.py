import os
from src.graph_loader import load_graph

json_path = os.path.join(
    os.path.dirname(__file__), "../data/city_graph.json"
)

graph = load_graph(json_path)
for node, neighbors in graph.items():
    print(node, "->", neighbors)

# ============
# TEST
# ============
def test_graph_loads():
    json_path = os.path.join(
        os.path.dirname(__file__), "../data/city_graph.json"
    )

    graph = load_graph(json_path)

    assert graph is not None
    assert len(graph) > 0

"""
Running: `python .\tests\test_loader.py` Gives Error of ModuleNotFoundError. For Correction, Changed The Import Path Of graph_loader.py
And city_graph.json
------------------
From The Root Directory
Run: `python -m tests.test_loader`
Test: `python -m pytest`
------------------
Python Supports Implicit Namespace Packages (PEP 420), Which Means A Directory Can Be Treated As A Package Even Without An __init__.py
That's Why `python -m tests.test_loader` Still Works
------------------
To Disable Bytecode Generation: `python -B -m tests.test_loader`
Or Put This At The Very Top Of The Script:
`
import sys
sys.dont_write_bytecode = True
`
------------------
The Most Common Approach Is Ignoring It In Git:
`
__pycache__/
*.py[cod]
`
------------------
"""
