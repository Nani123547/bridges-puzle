<<<<<<< HEAD
# puzzle.py

=======
>>>>>>> 147f787 (Updated project with latest code files)
from .island import Island
from .bridge import Bridge

class Puzzle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
<<<<<<< HEAD
        self.islands = []   # List of Island objects
        self.bridges = []   # List of Bridge objects
=======
        self.islands = []
        self.bridges = []
>>>>>>> 147f787 (Updated project with latest code files)

    def add_island(self, row, col, required_bridges):
        island = Island(row, col, required_bridges)
        self.islands.append(island)
        self.grid[row][col] = island

<<<<<<< HEAD
    def add_bridge(self, island1, island2, orientation, count=1):
        bridge = Bridge(island1, island2, orientation, count)
        self.bridges.append(bridge)
        island1.add_bridge(bridge)
        island2.add_bridge(bridge)
=======
    def valid_bridge(self, island1, island2, count=1):
        # Cant not connect the same island
        if island1 == island2:
            return False, "Cannot connect island to itself"
        
        if island1.row == island2.row:
            orientation = 'horizontal'
        elif island1.col == island2.col:
            orientation = 'vertical'
        else:
            return False, "Islands must be in the same row or column"
        
        if island1.current_bridges + count > island1.required_bridges:
            return False, "Island 1 exceeds required bridges"
        if island2.current_bridges + count > island2.required_bridges:
            return False, "Island 2 exceeds required bridges"
        
        existing_bridge = None
        for bridge in self.bridges:
            if (bridge.island1 == island1 and bridge.island2 == island2) or (bridge.island1 == island2 and bridge.island2 == island1):
                existing_bridge = bridge
                break
        if existing_bridge:
            if existing_bridge.count + count > 2:
                return False, "Cannot have more than 2 bridges between two islands"
        if orientation == 'horizontal':
            row = island1.row
            start = min(island1.col, island2.col) + 1
            end = max(island1.col, island2.col)
            for col in range(start, end):
                if self.grid[row][col] is not None:
                    return False, "Path blocked by an island"
        elif orientation == 'vertical':
            col = island1.col
            start = min(island1.row, island2.row) + 1
            end = max(island1.row, island2.row)
            for row in range(start, end):
                if self.grid[row][col] is not None:
                    return False, "Path blocked by an island"
        return True, orientation

    def add_bridge(self, island1, island2, count=1):
        valid, orientation_or_msg = self.valid_bridge(island1, island2, count)
        if not valid:
            return False, orientation_or_msg
        orientation = orientation_or_msg
        existing_bridge = None
        for bridge in self.bridges:
            if (bridge.island1 == island1 and bridge.island2 == island2) or (bridge.island1 == island2 and bridge.island2 == island1):
                existing_bridge = bridge
                break
        if existing_bridge:
            existing_bridge.count += count
            island1.current_bridges += count
            island2.current_bridges += count
        else:
            bridge = Bridge(island1, island2, orientation, count)
            self.bridges.append(bridge)
            island1.add_bridge(bridge)
            island2.add_bridge(bridge)
        return True, "Bridge added"
>>>>>>> 147f787 (Updated project with latest code files)

    def remove_bridge(self, bridge):
        if bridge in self.bridges:
            self.bridges.remove(bridge)
            bridge.island1.remove_bridge(bridge)
            bridge.island2.remove_bridge(bridge)

    def is_solved(self):
        return all(island.is_satisfied() for island in self.islands)

    def __repr__(self):
        return f"Puzzle({self.rows}x{self.cols}, Islands: {len(self.islands)}, Bridges: {len(self.bridges)})"
