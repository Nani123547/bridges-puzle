# island.py

class Island:
    def __init__(self, row, col, required_bridges):
        self.row = row
        self.col = col
        self.required_bridges = required_bridges
        self.current_bridges = 0
        self.bridges = []  # List to store connected Bridge objects

    def add_bridge(self, bridge):
        self.bridges.append(bridge)
        self.current_bridges += bridge.count

    def remove_bridge(self, bridge):
        if bridge in self.bridges:
            self.bridges.remove(bridge)
            self.current_bridges -= bridge.count

    def is_satisfied(self):
        return self.current_bridges == self.required_bridges

    def __repr__(self):
        return f"Island({self.row}, {self.col}, required: {self.required_bridges}, current: {self.current_bridges})"
