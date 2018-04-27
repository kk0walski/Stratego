from Board import Board

class BoardBackward(Board):
    moves = []

    def __init(self, size, player1=1,player2=2,board=None):
        super.__init__(size, player1, player2,board)

    def moveBackward(self, row, columm, color):
        points, warunek = self.move(row, columm, color)
        if warunek:
            self.moves.append((row, columm, color, points))

    def countZerosOdds(self, row, column):
        reasult = 0
        if len(self.getRowZeroPoints(self.board, row)) % 2 == 1:
            reasult += 1
        if len(self.getColumnZeroPoints(self.board, column)) % 2 == 1:
            reasult += 1
        _, positions = self.getDiagonalFirst(self.board, row, column)
        if len(positions) % 2 == 1:
            reasult += 1
        _, positions = self.getDiagonalSecond(self.board, row, column)
        if len(positions) % 2 == 1:
            reasult += 1

    def back(self):
        if len(self.moves) > 0:
            move = self.moves.pop()
            self.board[move[0],move[1]] = 0
            if self.player1Color == move[2]:
                self.player1 -= move[3]
            else:
                self.player2 -= move[3]