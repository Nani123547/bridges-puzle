# puzzle.py

from .island import Island
from .bridge import Bridge

class Puzzle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.islands = []   # List of Island objects
        self.bridges = []   # List of Bridge objects

    def add_island(self, row, col, required_bridges):
        island = Island(row, col, required_bridges)
        self.islands.append(island)
        self.grid[row][col] = island

    def add_bridge(self, island1, island2, orientation, count=1):
        bridge = Bridge(island1, island2, orientation, count)
        self.bridges.append(bridge)
        island1.add_bridge(bridge)
        island2.add_bridge(bridge)

    def remove_bridge(self, bridge):
        if bridge in self.bridges:
            self.bridges.remove(bridge)
            bridge.island1.remove_bridge(bridge)
            bridge.island2.remove_bridge(bridge)

    def is_solved(self):
        return all(island.is_satisfied() for island in self.islands)

    def __repr__(self):
        return f"Puzzle({self.rows}x{self.cols}, Islands: {len(self.islands)}, Bridges: {len(self.bridges)})"
