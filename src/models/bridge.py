# bridge.py

class Bridge:
    def __init__(self, island1, island2, orientation, count=1):
<<<<<<< HEAD
        self.island1 = island1  # Instance of Island
        self.island2 = island2  # Instance of Island
        self.orientation = orientation  # 'horizontal' or 'vertical'
        self.count = count  # Can be 1 or 2
=======
        self.island1 = island1 
        self.island2 = island2
        self.orientation = orientation 
        self.count = count
>>>>>>> 147f787 (Updated project with latest code files)

    def __repr__(self):
        return f"Bridge({self.island1.row},{self.island1.col} <-> {self.island2.row},{self.island2.col}, {self.orientation}, count: {self.count})"
