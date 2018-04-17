class Board:
    grid = []

    def __init__(self, size):
        for row in range(size):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(size):
                self.grid[row].append(0)  # Append a cell