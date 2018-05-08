from Board import Board

class BoardBackward(Board):
    moves = []

    def __init(self, size, player1=0,player2=0,board=None):
        super.__init__(size, player1, player2,board)

    def moveBackward(self, row, columm, color):
        points, warunek = self.move(row, columm, color)
        if points == 0:
            myRow = self.getRowZeroPoints(row, self.board)
            myColumn = self.getColumnZeroPoints(columm, self.board)
            list1, diagonalFirst = self.getDiagonalFirst(self.board, row, columm)
            list2, diagonalSecond = self.getDiagonalSecond(self.board, row, columm)
            if len(myRow) % 2 == 0 and len(myRow) != 0:
                points += list(self.board[row]).count(color)
            if len(myColumn) % 2 == 0 and len(myColumn) != 0:
                points += list(self.board[:, columm]).count(color)
            if len(diagonalFirst) % 2 == 0 and len(diagonalFirst) != 0:
                points += list(list1).count(color)
            if len(diagonalSecond)%2 == 0 and len(diagonalSecond) != 0:
                points += list(list2).count(color)
        if warunek:
            self.moves.append((row, columm, color, points))

    def getMoves(self):
        _, positions = self.getAllDiagonals(self.board)
        columnRows = self.getRowsColumnsPoints(self.board)
        filtr = list(filter(lambda p: len(p) % 2 == 1, positions + columnRows))
        filtr8 = list(filter(lambda p: len(p) <= self.size*0.8, filtr))
        filtr6 = list(filter(lambda p: len(p) <= self.size*0.6, filtr8))
        filtr4 = list(filter(lambda p: len(p) <= self.size*0.4, filtr6))
        filtr2 = list(filter(lambda p: len(p) <= self.size*0.2, filtr4))
        filtr = [i[0] for i in filtr]
        filtr8 = [i[0] for i in filtr8]
        filtr6 = [i[0] for i in filtr6]
        filtr4 = [i[0] for i in filtr4]
        filtr2 = [i[0] for i in filtr2]
        mySet = set(filtr)
        lista = list(mySet)
        mySet = set(filtr8)
        lista8 = list(mySet)
        mySet = set(filtr6)
        lista6 = list(mySet)
        mySet = set(filtr4)
        lista4 = list(mySet)
        mySet = set(filtr2)
        lista2 = list(mySet)
        if len(lista2) != 0:
            return lista2
        elif len(lista4) != 0:
            return lista4
        elif len(lista6) != 0:
            return lista6
        elif len(lista8) != 0:
            return lista8
        else:
            return lista

    def back(self):
        if len(self.moves) > 0:
            move = self.moves.pop()
            self.board[move[0],move[1]] = 0
            if self.player1Color == move[2]:
                self.player1 -= move[3]
            else:
                self.player2 -= move[3]