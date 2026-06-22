import time
from tests.manual.basic import run as basic_test
from tests.manual.edge_cases import run as edge_test
from tests.manual.correctness import run as correctness_test

def main():
    print("\nRunning Tests...\n")

    basic_test()
    time.sleep(1)
    edge_test()
    time.sleep(1)
    correctness_test()

    print("\n====================")
    print("ALL TESTS PASSED")
    print("====================")

if __name__ == "__main__":
    main()

"""
Running: `python .\\tests\\manual\\run_tests.py` Gives Error of ModuleNotFoundError

------------------

From Root Directory
Run: `python -m tests.manual.run_tests`
"""
