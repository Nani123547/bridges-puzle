# test_models.py

import unittest
from src.models.puzzle import Puzzle

class TestPuzzleModel(unittest.TestCase):
    def test_add_island(self):
        puzzle = Puzzle(5, 5)
        puzzle.add_island(1, 1, 2)
        self.assertEqual(len(puzzle.islands), 1)
        self.assertIsNotNone(puzzle.grid[1][1])

    def test_island_satisfaction(self):
        puzzle = Puzzle(5, 5)
        puzzle.add_island(2, 2, 2)
        island = puzzle.grid[2][2]
        self.assertFalse(island.is_satisfied())
        island.current_bridges = 2
        self.assertTrue(island.is_satisfied())

if __name__ == '__main__':
    unittest.main()
