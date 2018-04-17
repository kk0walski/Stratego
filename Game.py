from Board import Board
from GUI import GUI
import tkinter as tk

class Game:
    player1 = None
    player2 = None
    current_player = None
    board = None
    with_GUI = False

    def __init__(self, player1, player2, with_GUI=False):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = Board()
        self.with_GUI = with_GUI

        if self.with_GUI:
            master = tk.Tk()
            self.GUI = GUI(master)
            self.board.GUI = self.GUI
            self.player1.GUI = self.GUI
            self.player2.GUI = self.GUI

    def play(self):
        self.board.render()
        while not self.board.over():
            self.play_turn()
        self.declare_outcome()

    def play_turn(self):
        move = self.current_player.get_move()
        mark = self.current_player.mark
        self.board.place_mark(move, mark)
        self.switch_players()
        self.board.render()

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def declare_outcome(self):
        if self.board.winner() == 1:
            print("Player 1 wins!")
        elif self.board.winner() == 0:
            print("Player 2 wins!")
        else:
            print("Cat's game.")

