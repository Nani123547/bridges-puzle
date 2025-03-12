# bridge.py

class Bridge:
    def __init__(self, island1, island2, orientation, count=1):
        self.island1 = island1  # Instance of Island
        self.island2 = island2  # Instance of Island
        self.orientation = orientation  # 'horizontal' or 'vertical'
        self.count = count  # Can be 1 or 2

    def __repr__(self):
        return f"Bridge({self.island1.row},{self.island1.col} <-> {self.island2.row},{self.island2.col}, {self.orientation}, count: {self.count})"
