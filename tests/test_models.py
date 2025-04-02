<<<<<<< HEAD
# test_models.py

=======
>>>>>>> 147f787 (Updated project with latest code files)
import unittest
from src.models.puzzle import Puzzle

class TestPuzzleModel(unittest.TestCase):
    def test_add_island(self):
        puzzle = Puzzle(5, 5)
        puzzle.add_island(1, 1, 2)
        self.assertEqual(len(puzzle.islands), 1)
        self.assertIsNotNone(puzzle.grid[1][1])

<<<<<<< HEAD
    def test_island_satisfaction(self):
        puzzle = Puzzle(5, 5)
        puzzle.add_island(2, 2, 2)
        island = puzzle.grid[2][2]
        self.assertFalse(island.is_satisfied())
        island.current_bridges = 2
        self.assertTrue(island.is_satisfied())
=======
    def test_valid_bridge(self):
        puzzle = Puzzle(5, 5)
        puzzle.add_island(1, 1, 2)
        puzzle.add_island(1, 3, 3)
        island1 = puzzle.grid[1][1]
        island2 = puzzle.grid[1][3]
        valid, msg = puzzle.valid_bridge(island1, island2, 1)
        self.assertTrue(valid)
>>>>>>> 147f787 (Updated project with latest code files)

if __name__ == '__main__':
    unittest.main()
