# persistence.py

import json
from src.models.puzzle import Puzzle
from src.models.island import Island
from src.models.bridge import Bridge

def save_puzzle(puzzle, filename):
    data = {
        "rows": puzzle.rows,
        "cols": puzzle.cols,
        "islands": [
            {"row": island.row, "col": island.col, "required_bridges": island.required_bridges, "current_bridges": island.current_bridges}
            for island in puzzle.islands
        ],
        "bridges": [
            {
                "island1": {"row": bridge.island1.row, "col": bridge.island1.col},
                "island2": {"row": bridge.island2.row, "col": bridge.island2.col},
                "orientation": bridge.orientation,
                "count": bridge.count
            }
            for bridge in puzzle.bridges
        ]
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Puzzle saved to {filename}")

def load_puzzle(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    puzzle = Puzzle(data["rows"], data["cols"])
    island_dict = {}
    # Reconstruct islands
    for island_data in data["islands"]:
        island = Island(island_data["row"], island_data["col"], island_data["required_bridges"])
        island.current_bridges = island_data["current_bridges"]
        puzzle.islands.append(island)
        puzzle.grid[island.row][island.col] = island
        island_dict[(island.row, island.col)] = island
    # Reconstruct bridges
    for bridge_data in data["bridges"]:
        pos1 = (bridge_data["island1"]["row"], bridge_data["island1"]["col"])
        pos2 = (bridge_data["island2"]["row"], bridge_data["island2"]["col"])
        if pos1 in island_dict and pos2 in island_dict:
            island1 = island_dict[pos1]
            island2 = island_dict[pos2]
            bridge = Bridge(island1, island2, bridge_data["orientation"], bridge_data["count"])
            puzzle.bridges.append(bridge)
            island1.add_bridge(bridge)
            island2.add_bridge(bridge)
    print(f"Puzzle loaded from {filename}")
    return puzzle

if __name__ == "__main__":
    # Test persistence functions
    p = Puzzle(5, 5)
    p.add_island(1, 1, 2)
    p.add_island(2, 3, 3)
    save_puzzle(p, "test_puzzle.json")
    loaded_puzzle = load_puzzle("test_puzzle.json")
    print(loaded_puzzle)
