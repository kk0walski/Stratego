import pygame
import numpy as np

class Player:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 10
    HEIGHT = 10

    # This sets the margin between each cell
    MARGIN = 5

    color = 0

    def __init__(self, color):
        self.color = color

class Human(Player):

    def __init__(self, color):
        Player.__init__(self, color)

    def run(self, map_x, map_y, board):
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = (pos[0] - map_x) // (self.WIDTH + self.MARGIN)
        row = (pos[1] - map_y) // (self.HEIGHT + self.MARGIN)
        # Set that location to one
        return board.move(row, column, self.color)

class CompRandom(Player):

    def __init__(self, color):
        Player.__init__(self, color)

    def run(self, board):
        choice = np.random.choice(board.size, 2)
        return board.move(choice[0],choice[1], self.color)
