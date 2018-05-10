import pygame
import numpy as np
from BoardBackward import BoardBackward
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
        self.boardBack = None

    def run(self, board):
        self.boardBack = BoardBackward(size=self.size, board=board.board.copy())
        row, column, reasult = self.runPlayer(True, [(i,j) for i in range(self.size) for j in range(self.size) if board.board[i,j] == 0], 2, 0, -1)
        _, warunek = board.move(row,column, self.color)
        return [row, column], warunek

    def runPlayer(self, maximazing, lista, limit, floor, move=-1):
        if move != -1:
            self.boardBack.moveBackward(move[0], move[1], self.color if maximazing else 1 if self.color == 1 else 2)
        if len(lista) > 0 and floor < limit:
            if maximazing:
                bestValue = float("-inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, lista[0:i] + lista[i + 1:], limit, floor, lista[i])
                    bestValue = max(bestValue, v)
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
            else:
                bestValue = float("inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, lista[0:i] + lista[i + 1:], limit, floor, lista[i])
                    bestValue = min(bestValue, v)
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
        else:
            reasult = self.boardBack.moves[-1]
            self.boardBack.back()
            return reasult[0], reasult[1], reasult[3]


class AlfaBeta(Player):

    def __init__(self, color, size):
        Player.__init__(self, color)
        self.size = size
        self.boardBack = None

    def run(self, board):
        self.boardBack = BoardBackward(size=self.size, board=board.board.copy())
        row, column, reasult = self.runPlayer(True, float("-inf"), float("inf"), [(i,j) for i in range(self.size) for j in range(self.size) if board.board[i,j] == 0], 2, 0, -1)
        _, warunek = board.move(row,column, self.color)
        return [row, column], warunek

    def runPlayer(self, maximazing, alfa, beta, lista, limit, floor, move=-1):
        if move != -1:
            self.boardBack.moveBackward(move[0], move[1], self.color if maximazing else 1 if self.color == 1 else 2)
        if len(lista) > 0 and floor < limit:
            if maximazing:
                bestValue = float("-inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, alfa, beta, lista[0:i] + lista[i + 1:], limit, floor, lista[i])
                    bestValue = max(bestValue, v)
                    alfa = max(alfa,bestValue)
                    if beta <= alfa:
                        break
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
            else:
                bestValue = float("inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, alfa, beta, lista[0:i] + lista[i + 1:], limit, floor, lista[i])
                    bestValue = min(bestValue, v)
                    beta = min(beta, bestValue)
                    if beta <= alfa:
                        break
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
        else:
            reasult = self.boardBack.moves[-1]
            self.boardBack.back()
            return reasult[0], reasult[1], reasult[3]

class MinMaxOdd(Player):

    def __init__(self, color, size):
        Player.__init__(self, color)
        self.size = size
        self.boardBack = None

    def run(self, board):
        self.boardBack = BoardBackward(size=self.size, board=board.board.copy())
        row, column, reasult = self.runPlayer(True, self.boardBack.getMoves(), 3, 0, -1)
        _, warunek = board.move(row,column, self.color)
        return [row, column], warunek

    def runPlayer(self, maximazing, lista, limit, floor, move=-1):
        if move != -1:
            self.boardBack.moveBackward(move[0], move[1], self.color if maximazing else 1 if self.color == 1 else 2)
            lista = self.boardBack.getMoves()
        if len(lista) > 0 and floor < limit:
            if maximazing:
                bestValue = float("-inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, lista[0:i] + lista[i + 1:], limit, floor, lista[i])
                    bestValue = max(bestValue, v)
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
            else:
                bestValue = float("inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, lista[0:i] + lista[i + 1:], limit, floor, lista[i])
                    bestValue = min(bestValue, v)
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
        else:
            reasult = self.boardBack.moves[-1]
            self.boardBack.back()
            return reasult[0], reasult[1], reasult[3]

class AlfaBetaOdd(Player):
    def __init__(self, color, size):
        Player.__init__(self, color)
        self.size = size
        self.boardBack = None

    def run(self, board):
        self.boardBack = BoardBackward(size=self.size, board=board.board.copy())
        row, column, reasult = self.runPlayer(True, float("-inf"), float("inf"), 4, 0, -1)
        _, warunek = board.move(row, column, self.color)
        return [row, column], warunek

    def runPlayer(self, maximazing, alfa, beta, limit, floor, move = -1):
        if move != -1:
            self.boardBack.moveBackward(move[0], move[1], self.color if maximazing else 1 if self.color == 1 else 2)
            lista = self.boardBack.getMoves()
        else:
            lista = self.boardBack.getMoves()
        if len(lista) > 0 and floor < limit:
            if maximazing:
                bestValue = float("-inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, alfa, beta, limit, floor, lista[i])
                    bestValue = max(bestValue, v)
                    alfa = max(alfa, bestValue)
                    if beta <= alfa:
                        break
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
            else:
                bestValue = float("inf")
                floor += 1
                for i in range(len(lista)):
                    row, column, v = self.runPlayer(not maximazing, alfa, beta, limit, floor, lista[i])
                    bestValue = min(bestValue, v)
                    beta = min(beta, bestValue)
                    if beta <= alfa:
                        break
                self.boardBack.back()
                if move != -1:
                    return move[0], move[1], bestValue
                else:
                    return row, column, bestValue
        else:
            reasult = self.boardBack.moves[-1]
            self.boardBack.back()
            return reasult[0], reasult[1], reasult[3]
