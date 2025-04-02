<<<<<<< HEAD
# ui.py

=======
>>>>>>> 147f787 (Updated project with latest code files)
import tkinter as tk
from tkinter import messagebox
from src.models.puzzle import Puzzle

CELL_SIZE = 60

class PuzzleUI:
    def __init__(self, master, puzzle):
        self.master = master
        self.puzzle = puzzle
<<<<<<< HEAD
=======
        self.selected_island = None
>>>>>>> 147f787 (Updated project with latest code files)
        self.canvas = tk.Canvas(master, width=puzzle.cols * CELL_SIZE, height=puzzle.rows * CELL_SIZE, bg="white")
        self.canvas.pack()
        self.draw_grid()
        self.draw_islands()
<<<<<<< HEAD
        # Bind left mouse click to handle clicks on the canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_grid(self):
=======
        self.draw_bridges()
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_grid(self):
        self.canvas.delete("grid")
>>>>>>> 147f787 (Updated project with latest code files)
        for i in range(self.puzzle.rows):
            for j in range(self.puzzle.cols):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
<<<<<<< HEAD
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

    def draw_islands(self):
=======
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray", tags="grid")

    def draw_islands(self):
        self.canvas.delete("island")
>>>>>>> 147f787 (Updated project with latest code files)
        for island in self.puzzle.islands:
            x = island.col * CELL_SIZE + CELL_SIZE // 2
            y = island.row * CELL_SIZE + CELL_SIZE // 2
            r = CELL_SIZE // 4
<<<<<<< HEAD
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightblue")
            self.canvas.create_text(x, y, text=str(island.required_bridges), fill="black", font=("Arial", 16, "bold"))
=======
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightblue", tags="island")
            self.canvas.create_text(x, y, text=str(island.required_bridges), fill="black", font=("Arial", 16, "bold"), tags="island")
    
    def draw_bridges(self):
        self.canvas.delete("bridge")
        for bridge in self.puzzle.bridges:
            x1 = bridge.island1.col * CELL_SIZE + CELL_SIZE // 2
            y1 = bridge.island1.row * CELL_SIZE + CELL_SIZE // 2
            x2 = bridge.island2.col * CELL_SIZE + CELL_SIZE // 2
            y2 = bridge.island2.row * CELL_SIZE + CELL_SIZE // 2
            if bridge.count == 1:
                self.canvas.create_line(x1, y1, x2, y2, width=4, fill="black", tags="bridge")
            elif bridge.count == 2:
                if bridge.orientation == 'horizontal':
                    self.canvas.create_line(x1, y1 - 4, x2, y2 - 4, width=4, fill="black", tags="bridge")
                    self.canvas.create_line(x1, y1 + 4, x2, y2 + 4, width=4, fill="black", tags="bridge")
                else:  # vertical
                    self.canvas.create_line(x1 - 4, y1, x2 - 4, y2, width=4, fill="black", tags="bridge")
                    self.canvas.create_line(x1 + 4, y1, x2 + 4, y2, width=4, fill="black", tags="bridge")
>>>>>>> 147f787 (Updated project with latest code files)

    def on_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
<<<<<<< HEAD
        messagebox.showinfo("Cell Clicked", f"You clicked on cell ({row}, {col})")
        # Future work: Add logic for drawing bridges on click events
=======
        clicked_island = None
        for island in self.puzzle.islands:
            if island.row == row and island.col == col:
                clicked_island = island
                break
        if clicked_island:
            if self.selected_island is None:
                self.selected_island = clicked_island
                messagebox.showinfo("Selection", f"Selected island at ({row}, {col})")
            else:
                if self.selected_island == clicked_island:
                    self.selected_island = None
                    messagebox.showinfo("Selection", "Deselected island")
                else:
                    success, msg = self.puzzle.add_bridge(self.selected_island, clicked_island, count=1)
                    if success:
                        messagebox.showinfo("Bridge", f"Bridge added between ({self.selected_island.row}, {self.selected_island.col}) and ({clicked_island.row}, {clicked_island.col})")
                    else:
                        messagebox.showerror("Error", msg)
                    self.selected_island = None
                    self.draw_bridges()
        else:
            self.selected_island = None
>>>>>>> 147f787 (Updated project with latest code files)

def main():
    root = tk.Tk()
    root.title("Bridges Puzzle Solver")
<<<<<<< HEAD
    # Create a sample puzzle for demonstration
=======
    
>>>>>>> 147f787 (Updated project with latest code files)
    puzzle = Puzzle(5, 5)
    puzzle.add_island(1, 1, 2)
    puzzle.add_island(1, 3, 3)
    puzzle.add_island(3, 2, 2)
    app = PuzzleUI(root, puzzle)
    root.mainloop()

if __name__ == "__main__":
    main()
