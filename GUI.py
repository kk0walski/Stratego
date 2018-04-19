import pygame
from Player import Player
from Board import Board

class GUI:
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 10
    HEIGHT = 10

    # This sets the margin between each cell
    MARGIN = 5

    TOURN = 1

    clock = 0

    size = 0

    screen = 0
    main_map = 0

    window_width = 0
    window_height = 0

    map_width = 0
    map_height = 0

    done = False

    map_x = 0  # Only this should change
    map_y = 0
    # The change for x
    map_x_c = -3

    player1 = None
    player2 = None
    board = None

    def __init__(self, size, window_width, window_height):
        self.clock = pygame.time.Clock()
        self.board = Board(size)

        self.size = size
        self.window_width = window_width
        self.window_height = window_height

        # Set the HEIGHT and WIDTH of the screen
        map_width = size*50
        map_height = size*50

        # Initialize pygame
        pygame.init()
        WINDOW_SIZE = [window_width, window_height]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Array Backed Grid")
        self.main_map = pygame.Surface((map_width, map_height))
        self.main_map = self.main_map.convert()

        self.screen.blit(self.main_map, (self.map_x, self.map_y, window_width, window_height))
        pygame.display.flip()
        self.player1 = Player(1)
        self.player2 = Player(2)

    def draw(self):
        for row in range(self.size):
            for column in range(self.size):
                color = self.WHITE
                if self.board.getField(row,column) == 1:
                    color = self.GREEN
                if self.board.getField(row,column) == 2:
                    color = self.RED
                pygame.draw.rect(self.main_map,
                                 color,
                                 [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])

        # -------- Main Program Loop -----------
    def run(self):
        pass

gra = GUI(10, 300, 300)
gra.run()