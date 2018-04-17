"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

SIZE = 50

window_width = 800
window_height = 600

map_width = 2540
map_height = 2540

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(SIZE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(SIZE):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [window_width,  window_height]
screen = pygame.display.set_mode(WINDOW_SIZE)
main_map = pygame.Surface((map_width, map_height))
main_map = main_map.convert()

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

map_x = 0  # Only this should change
map_y = 0
# The change for x
map_x_c = -3
screen.blit(main_map, (map_x, map_y, window_width, window_height))
pygame.display.flip()
print(map_x, map_y, map_x + window_width, map_y + window_height)

def draw():
    for row in range(SIZE):
        for column in range(SIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(main_map,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0] - map_x) // (WIDTH + MARGIN)
            row = (pos[1] - map_y) // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:  # and map_x != 0:
        map_x -= map_x_c
        print(map_x, map_y, map_x + window_width, map_y + window_height)
    elif key_pressed[pygame.K_RIGHT]:
        map_x += map_x_c
        print(map_x, map_y, map_x + window_width, map_y + window_height)
    elif key_pressed[pygame.K_UP]:
        map_y -= map_x_c
        print(map_x, map_y, map_x + window_width, map_y + window_height)
    elif key_pressed[pygame.K_DOWN]:
        map_y += map_x_c
        print(map_x, map_y, map_x + window_width, map_y + window_height)

    # Set the screen background
    main_map.fill(BLACK)

    # Draw the grid
    draw()
    screen.blit(main_map, (map_x, map_y, window_width, window_height))
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()