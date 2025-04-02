<<<<<<< HEAD
# test_solver.py

=======
>>>>>>> 147f787 (Updated project with latest code files)
import unittest
from src.models.puzzle import Puzzle
from src.solver.solver import solve_puzzle

class TestSolver(unittest.TestCase):
    def test_solver_stub(self):
        puzzle = Puzzle(5, 5)
        puzzle.add_island(1, 1, 2)
        puzzle.add_island(1, 3, 3)
        result = solve_puzzle(puzzle)
<<<<<<< HEAD
        # Since our solver is a stub, it always returns False
=======
>>>>>>> 147f787 (Updated project with latest code files)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
