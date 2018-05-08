import numpy as np

class Board:
    board = None
    size = 0
    player1 = 0
    player2 = 0
    player1Color = 1
    player2Color = 2

    def __init__(self, size, player1=0,player2=0,board=None):
        self.size = size
        if board is None:
            self.board = np.zeros(shape=(self.size, self.size), dtype=np.int)
        else:
            self.board = board
        self.player1=player1
        self.player2=player2

    def clone(self):
        return self.__init__(self.size, self.player1, self.player2,np.copy(self.board))

    def move(self, row, columm, color):
        points = 0
        if row < self.size and row >= 0 and columm < self.size and columm >= 0:
            if self.board[row,columm] == 0:
                self.board[row,columm] = color
                points = self.getPoints(row, columm, color)
                if self.player1Color == color:
                    self.player1 += points
                else:
                    self.player2 += points
                return points, True
            else:
                return points, False
        else:
            return points, False

    def getField(self, row, column):
        return self.board[row,column]

    def getDiagonalFirst(self, board, row, column):
        lista = []
        positions = []
        for i in range(1,self.size):
            if row-i >= 0 and column-i >= 0:
                if board[row - i, column - i] == 0:
                    positions.append((row-i,column-i))
                lista.append(board[row-i,column-i])
            if row+i < self.size and column+i < self.size:
                if board[row + i, column + i] == 0:
                    positions.append((row + i, column + i))
                lista.append(board[row + i, column + i])
        lista.append(board[row,column])
        if board[row,column] == 0:
            positions.append((row,column))
        return lista, positions

    def getDiagonalSecond(self, board, row, column):
        lista = []
        positions = []
        for i in range(1, self.size):
            if row - i >= 0 and column + i < self.size:
                if board[row - i, column + i] == 0:
                    positions.append((row-i,column+i))
                lista.append(board[row - i, column + i])
            if row + i < self.size and column - i >= 0:
                if board[row + i, column - i] == 0:
                    positions.append((row+i,column-i))
                lista.append(board[row + i, column - i])
        lista.append(board[row, column])
        if board[row,column] == 0:
            positions.append((row,column))
        return lista, positions

    def getDiagonals(self, board, row, column):
        lista1, columns1 = self.getDiagonalFirst(board,row,column)
        lista2, columns2 = self.getDiagonalSecond(board, row, column)
        return [lista1,lista2],[columns1,columns2]

    def getAllDiagonals(self, board):
        lists = []
        columns = []
        for i in range(self.size):
            listTemp,columnTemp = self.getDiagonals(board, i, 0)
            lists += listTemp
            columns += columnTemp
            listTemp, columnTemp = self.getDiagonals(board, self.size - 1, i)
            lists += listTemp
            columns += columnTemp
            listTemp, columnTemp = self.getDiagonals(board, i, self.size-1)
            lists += listTemp
            columns += columnTemp
            listTemp, columnTemp = self.getDiagonals(board, 0, i)
            lists += listTemp
            columns += columnTemp
        return lists, columns

    def getRowsColumnsPoint(self, board):
        for i in range(self.size):
            lista = list(board[i])
            if lista.count(0) == 1:
                return (i,lista.index(0))
            lista = list(board[:,i])
            if lista.count(0) == 1:
                return (lista.index(0),i)
        return (-1,-1)

    def getRowZeroPoints(self, row, board):
        positions = []
        if row < self.size and row >= 0:
            myRow = board[row]
            for i in range(0, self.size):
                if myRow[i] == 0:
                    positions.append((row,i))
        return positions

    def getColumnZeroPoints(self, column,board):
        positions = []
        if column < self.size and column >= 0:
            myColumn = board[:,column]
            for i in range(0, self.size):
                if myColumn[i] == 0:
                    positions.append((i,column))
        return positions

    def getRowsColumnsPoints(self, board):
        reasult = []
        for i in range(self.size):
            reasult.append(self.getRowZeroPoints(i, board))
            reasult.append(self.getColumnZeroPoints(i, board))
        return reasult


    def getPoints(self, row, column, color):
        points = 0
        if list(self.board[row]).count(0) == 0:
            points += list(self.board[row]).count(color)
        if list(self.board[:,column]).count(0) == 0:
            points += list(self.board[:,column]).count(color)
        diagonal1, temp = self.getDiagonalFirst(self.board, row, column)
        if diagonal1.count(0) == 0 and len(diagonal1) > 1:
            points += diagonal1.count(color)
        diagonal2, temp = self.getDiagonalSecond(self.board, row, column)
        if diagonal2.count(0) == 0 and len(diagonal2) > 1:
            points += diagonal2.count(color)
        return points

    def isEnd(self):
        return np.count_nonzero(self.board == 0) == 0

    def getState(self):
        return "Player1: " + str(self.player1) + " Player2: " + str(self.player2)
