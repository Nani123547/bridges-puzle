# ui.py

import tkinter as tk
from tkinter import messagebox
from src.models.puzzle import Puzzle

CELL_SIZE = 60

class PuzzleUI:
    def __init__(self, master, puzzle):
        self.master = master
        self.puzzle = puzzle
        self.canvas = tk.Canvas(master, width=puzzle.cols * CELL_SIZE, height=puzzle.rows * CELL_SIZE, bg="white")
        self.canvas.pack()
        self.draw_grid()
        self.draw_islands()
        # Bind left mouse click to handle clicks on the canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_grid(self):
        for i in range(self.puzzle.rows):
            for j in range(self.puzzle.cols):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

    def draw_islands(self):
        for island in self.puzzle.islands:
            x = island.col * CELL_SIZE + CELL_SIZE // 2
            y = island.row * CELL_SIZE + CELL_SIZE // 2
            r = CELL_SIZE // 4
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightblue")
            self.canvas.create_text(x, y, text=str(island.required_bridges), fill="black", font=("Arial", 16, "bold"))

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        messagebox.showinfo("Cell Clicked", f"You clicked on cell ({row}, {col})")
        # Future work: Add logic for drawing bridges on click events

def main():
    root = tk.Tk()
    root.title("Bridges Puzzle Solver")
    # Create a sample puzzle for demonstration
    puzzle = Puzzle(5, 5)
    puzzle.add_island(1, 1, 2)
    puzzle.add_island(1, 3, 3)
    puzzle.add_island(3, 2, 2)
    app = PuzzleUI(root, puzzle)
    root.mainloop()

if __name__ == "__main__":
    main()
