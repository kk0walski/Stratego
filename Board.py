import numpy as np

class Board:
    grid = None
    GUI = None

    def __init__(self, grid = np.zeros((3,3)).astype(int), GUI=None):
        self.grid = grid
        self.GUI = GUI

    def move(self, x, y, color):
        try:
            if self.grid[x,y] == 0:
                self.grid[x,y] = color
        except IndexError:
            return

board = Board()
print(board.move(5,5,1))