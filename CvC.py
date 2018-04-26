import pygame
from GUI import GUI
from Player import CompRandom, CompRandomDiagonals, oddPlayer


class CvC(GUI):

    def __init__(self, size, window_width, window_height):
        GUI.__init__(self, size, window_width, window_height)
        self.player1 = oddPlayer(1)
        self.player2 = CompRandomDiagonals(2)

    def run(self):
        while not self.done:
            move = [0, 0]
            if self.TOURN == 1:
                move, warunek = self.player1.run(self.board)
                if warunek:
                    print(self.board.getState())
                    self.done = self.board.isEnd()
                    self.TOURN = 2
            else:
                move, warunek = self.player2.run(self.board)
                if warunek:
                    print(self.board.getState())
                    self.done = self.board.isEnd()
                    self.TOURN = 1

            # Set the screen background
            self.main_map.fill(self.BLACK)

            # Draw the grid
            self.draw()
            self.screen.blit(self.main_map, (self.map_x, self.map_y, self.window_width, self.window_height))
            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Be IDLE friendly. If you forget this line, the program will 'hang'
            # on exit.
        pygame.quit()


gra = CvC(50, 500, 500)
gra.run()
