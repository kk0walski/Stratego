from Board import Board

class BoardBackward(Board):
    moves = []

    def __init(self, size, player1=0,player2=0,board=None):
        super.__init__(size, player1, player2,board)

    def moveBackward(self, row, columm, color):
        points = 0
        myPoints, warunek = self.move(row, columm, color)
        myRow = self.getRowZeroPoints(row, self.board)
        myColumn = self.getColumnZeroPoints(columm, self.board)
        # list1, diagonalFirst = self.getDiagonalFirst(self.board, row, columm)
        # list2, diagonalSecond = self.getDiagonalSecond(self.board, row, columm)
        # if len(myRow) % 2 == 0 and len(myRow) != 0:
        #     points += (self.board[row] == color).sum()
        # if len(myColumn) % 2 == 0 and len(myColumn) != 0:
        #      points += (self.board[:, columm] == color).sum()
        # if len(diagonalFirst) % 2 == 0 and len(diagonalFirst) != 0:
        #     points += list(list1).count(color)
        # if len(diagonalSecond)%2 == 0 and len(diagonalSecond) != 0:
        #     points += list(list2).count(color)
        if warunek:
            if color == self.player1Color:
                points += self.player1 - self.player2
            else:
                points += self.player2 - self.player1
            self.moves.append((row, columm, color, myPoints, points))

    def getMovePoints(self, lista, color):
        self.moveBackward(lista[0][0],lista[0][1], color)
        reasult = self.moves[-1]
        points = reasult[4]
        self.back()
        best = 0
        if points > 0:
            best = 0 - points
        else:
            best = len(lista)
        return best

    def getMoves(self, color):
        _, positions = self.getAllDiagonals(self.board)
        columnRows = self.getRowsColumnsPoints(self.board)
        filtr = list(filter(lambda p: len(p) % 2 == 1, positions + columnRows))
        filtr = sorted(filtr, key=lambda p: self.getMovePoints(lista=p, color=color))
        procenty = [i for i in range(1,101)]
        for i in procenty:
            filtr2 = list(filter(lambda p: len(p) <= (self.size**(1/2)) * i, filtr))
            filtr2 = [i[0] for i in filtr2]
            if len(filtr2) != 0:
                return filtr2
        return [i[0] for i in filtr]

    def back(self):
        if len(self.moves) > 0:
            move = self.moves.pop()
            self.board[move[0],move[1]] = 0
            if self.player1Color == move[2]:
                self.player1 -= move[3]
            else:
                self.player2 -= move[3]