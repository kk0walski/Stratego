import pygame
import numpy as np
from anytree import Node, RenderTree

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
        _, warunek = board.move(row, column, self.color)
        return pos, warunek

class CompRandom(Player):

    def __init__(self, color):
        Player.__init__(self, color)

    def run(self, board):
        choice = np.random.choice(board.size, 2)
        column = choice[0] * (self.WIDTH + self.MARGIN)
        row = choice[1] * (self.HEIGHT + self.MARGIN)
        _,warunek = board.move(choice[0],choice[1], self.color)
        return [column, row], warunek

class CompRandomDiagonals(Player):

    def __init__(self, color):
        Player.__init__(self, color)

    def run(self, board):
        _, positions = board.getAllDiagonals(board.board)
        tupla = board.getRowsColumnsPoint(board.board)
        positions.append(tupla)
        filtr = list(filter(lambda p: len(p) == 1, positions))
        if len(filtr) > 0:
            column = filtr[0][0][0]*(self.WIDTH + self.MARGIN)
            row = filtr[0][0][1]*(self.HEIGHT + self.MARGIN)
            _, warunek = board.move(filtr[0][0][0],filtr[0][0][1], self.color)
            return [column, row], warunek
        else:
            choice = np.random.choice(board.size, 2)
            column = choice[0] * (self.WIDTH + self.MARGIN)
            row = choice[1] * (self.HEIGHT + self.MARGIN)
            _,warunek = board.move(choice[0],choice[1], self.color)
            return [column, row], warunek

class oddPlayer(Player):

    def __init__(self, color):
        Player.__init__(self, color)

    def run(self, board):
        _, positions = board.getAllDiagonals(board.board)
        columnRows = board.getRowsColumnsPoints(board.board)
        filtr = list(filter(lambda p: len(p)%2 == 1, positions + columnRows))
        filtr = sorted(filtr, key=len)
        filtr2 = list(filter(lambda p: len(p) == 1, filtr))
        filtr3 = list(filter(lambda p: len(p) != 1, filtr))
        if len(filtr2) > 0:
            column = filtr2[0][0][0] * (self.WIDTH + self.MARGIN)
            row = filtr2[0][0][1] * (self.HEIGHT + self.MARGIN)
            _,warunek = board.move(filtr2[0][0][0], filtr2[0][0][1], self.color)
            return [column, row], warunek
        if len(filtr3) > 0:
            column = filtr3[0][0][0]*(self.WIDTH + self.MARGIN)
            row = filtr3[0][0][1]*(self.HEIGHT + self.MARGIN)
            _,warunek = board.move(filtr3[0][0][0],filtr3[0][0][1], self.color)
            return [column, row], warunek

class MinMax(Player):

    def __init__(self, color, size):
        Player.__init__(self, color)
        self.size = size
        if color == 1:
            self.color2 = 2
        else:
            self.color2 = 1
            [(i,j) for i in range(size) for j in range(size)]
        self.root = self.createTree(Node(name=(0,0), ocena=0), [(i,j) for i in range(size) for j in range(size)], 5, 0)

    def createTree(self, root, list, limit, floor):
        if len(list) and floor < limit:
            floor+=1
            root.children = [self.createTree(Node(name=list[i], ocena=0, parent=root), list[i+1:], limit, floor) for i in range(len(list))]
            return root
        else:
            return root



player = MinMax(1, 5)