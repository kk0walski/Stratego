import tkinter as tk

class GUI:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(frame, height=3, width=3, text="", command=lambda i=i, j=j: self.make_move(self.buttons[i][j]))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, button):
        if button["text"] == "":
            button.configure(text="X")
        info = button.grid_info()
        move = (info["row"], info["column"])
        print(move)
        return move