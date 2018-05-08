from Board import Board

class BoardBackward(Board):
    moves = []

    def __init(self, size, player1=1,player2=2,board=None):
        super.__init__(size, player1, player2,board)

    def moveBackward(self, row, columm, color):
        points, warunek = self.move(row, columm, color)
        if points == 0:
            myRow = self.getRowZeroPoints(row, self.board)
            myColumn = self.getColumnZeroPoints(columm, self.board)
            if len(myRow) % 2 == 0 and len(myRow) != 0:
                points += list(self.board[row]).count(color)
            if len(myColumn) % 2 == 0 and len(myColumn) != 0:
                points += list(self.board[:, columm]).count(color)
        else:
            points = points*self.size
        # list1, diagonalFirst = self.getDiagonalFirst(self.board, row, columm)
        # list2, diagonalSecond = self.getDiagonalSecond(self.board, row, columm)
        # if len(diagonalFirst)%2 == 0 and len(diagonalFirst) != 0:
        #     points += list(list1).count(color)
        # if len(diagonalSecond)%2 == 0 and len(diagonalSecond) != 0:
        #     points += list(list2).count(color)
        if warunek:
            self.moves.append((row, columm, color, points))

    def getMoves(self):
        _, positions = self.getAllDiagonals(self.board)
        columnRows = self.getRowsColumnsPoints(self.board)
        filtr = list(filter(lambda p: len(p) % 2 == 1, positions + columnRows))
        filtr75 = list(filter(lambda p: len(p) <= self.size*0.75, filtr))
        filtr5 = list(filter(lambda p: len(p) <= self.size*0.5, filtr75))
        filtr25 = list(filter(lambda p: len(p) <= self.size*0.25, filtr5))
        filtr10 = list(filter(lambda p: len(p) <= self.size*0.1, filtr5))
        filtr = [i[0] for i in filtr]
        filtr75 = [i[0] for i in filtr75]
        filtr5 = [i[0] for i in filtr5]
        filtr25 = [i[0] for i in filtr25]
        filtr10 = [i[0] for i in filtr10]
        mySet = set(filtr)
        lista = list(mySet)
        mySet = set(filtr75)
        lista75 = list(mySet)
        mySet = set(filtr5)
        lista5 = list(mySet)
        mySet = set(filtr25)
        lista25 = list(mySet)
        mySet = set(filtr10)
        lista10 = list(mySet)
        if len(lista10) != 0:
            return lista10
        elif len(lista25) != 0:
            return lista25
        elif len(lista5) != 0:
            return lista5
        elif len(lista75) != 0:
            return lista75
        else:
            print(lista)
            return lista

    def back(self):
        if len(self.moves) > 0:
            move = self.moves.pop()
            self.board[move[0],move[1]] = 0
            if self.player1Color == move[2]:
                self.player1 -= move[3]
            else:
                self.player2 -= move[3]