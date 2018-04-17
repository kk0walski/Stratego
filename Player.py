import pygame

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

    def run(self, grid, map_x, map_y):
        count = 0
        for event in pygame.event.get():  # User did something
            if event.type == pygame.MOUSEBUTTONDOWN and count < 1:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = (pos[0] - map_x) // (self.WIDTH + self.MARGIN)
                row = (pos[1] - map_y) // (self.HEIGHT + self.MARGIN)
                # Set that location to one
                if grid[row][column] == 0:
                    count += 1
                    grid[row][column] = self.color
                    break
