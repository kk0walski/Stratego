import pygame
from Player import Player


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

    PLAYER_VS_PLAYER = 0
    PLAYER_VS_MACHINE = 1
    MACHINE_VS_PLAYER = 2
    MACHINE_VS_MACHINE = 3

    players = 0

    clock = 0

    size = 0

    screen = 0
    main_map = 0

    window_width = 0
    window_height = 0

    map_width = 0
    map_height = 0

    done = False

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []

    map_x = 0  # Only this should change
    map_y = 0
    # The change for x
    map_x_c = -3

    player1 = None
    player2 = None

    def __init__(self, size, window_width, window_height):
        self.player1 = Player(1)
        self.player2 = Player(2)
        if self.player1.isHuman() and not self.player2.isHuman():
            self.players = self.PLAYER_VS_MACHINE
        elif not self.player1.isHuman() and self.player2.isHuman():
            self.players = self.MACHINE_VS_PLAYER
        elif not self.player1.isHuman() and not self.player2.isHuman():
            self.players = self.MACHINE_VS_MACHINE

        self.clock = pygame.time.Clock()
        for row in range(size):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(size):
                self.grid[row].append(0)  # Append a cell

        self.size = size
        self.window_width = window_width
        self.window_height = window_height
        # Initialize pygame
        pygame.init()
        WINDOW_SIZE = [window_width, window_height]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Array Backed Grid")

        # Set the HEIGHT and WIDTH of the screen
        map_width = size*50
        map_height = size*50

        WINDOW_SIZE = [window_width, window_height]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.main_map = pygame.Surface((map_width, map_height))
        self.main_map = self.main_map.convert()

        self.screen.blit(self.main_map, (self.map_x, self.map_y, window_width, window_height))
        pygame.display.flip()

    def draw(self):
        for row in range(self.size):
            for column in range(self.size):
                color = self.WHITE
                if self.grid[row][column] == 1:
                    color = self.GREEN
                if self.grid[row][column] == 2:
                    color = self.RED
                pygame.draw.rect(self.main_map,
                                 color,
                                 [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT])

        # -------- Main Program Loop -----------
    def run(self):
        while not self.done:
            for event in pygame.event.get():  # User did something
                if self.TOURN == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.player1.run(self.map_x, self.map_y, self.grid, self.size):
                            self.TOURN = 2
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.player2.run(self.map_x, self.map_y, self.grid, self.size):
                            self.TOURN = 1

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT]:  # and map_x != 0:
                self.map_x -= self.map_x_c
            elif key_pressed[pygame.K_RIGHT]:
                self.map_x += self.map_x_c
            elif key_pressed[pygame.K_UP]:
                self.map_y -= self.map_x_c
            elif key_pressed[pygame.K_DOWN]:
                self.map_y += self.map_x_c
            elif key_pressed[pygame.K_ESCAPE]:
                quit()

            # Set the screen background
            self.main_map.fill(self.BLACK)

            # Draw the grid
            self.draw()
            self.screen.blit(self.main_map, (self.map_x, self.map_y, self.window_width, self.window_height))
            # Limit to 60 frames per second
            self.clock.tick(80)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Be IDLE friendly. If you forget this line, the program will 'hang'
            # on exit.
        pygame.quit()

gra = GUI(10, 300, 300)
gra.run()