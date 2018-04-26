from Board import Board

class BoardBackward(Board):
    moves = []

    def __init(self, size, player1=0,player2=0,board=None):
        super.__init__(size, player1, player2,board)

    def moveBackward(self, row, columm, color):
        if self.move(row, columm, color):
            self.moves.append((row, columm))

    def back(self):
        move = self.moves.pop()
        self.board[move[0],move[1]] = 0