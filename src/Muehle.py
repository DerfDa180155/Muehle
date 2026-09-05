import pygame


class Muehle:
    def __init__(self):
        self.board = self.generateEmptyBoard()

        self.phase = 0
        self.playerTurn = "w"

    def generateEmptyBoard(self):
        return [["o", "-", "-", "-", "-", "-", "o", "-", "-", "-", "-", "-", "o"],
                ["|", "", "", "", "", "", "|", "", "", "", "", "", "|"],
                ["|", "", "o", "-", "-", "-", "o", "-", "-", "-", "o", "", "|"],
                ["|", "", "|", "", "", "", "|", "", "", "", "|", "", "|"],
                ["|", "", "|", "", "o", "-", "o", "-", "o", "", "|", "", "|"],
                ["|", "", "|", "", "|", "", "", "", "|", "", "|", "", "|", ],
                ["o", "-", "o", "-", "o", "", "", "", "o", "-", "o", "-", "o"],
                ["|", "", "|", "", "|", "", "", "", "|", "", "|", "", "|", ],
                ["|", "", "|", "", "o", "-", "o", "-", "o", "", "|", "", "|"],
                ["|", "", "|", "", "", "", "|", "", "", "", "|", "", "|"],
                ["|", "", "o", "-", "-", "-", "o", "-", "-", "-", "o", "", "|"],
                ["|", "", "", "", "", "", "|", "", "", "", "", "", "|"],
                ["o", "-", "-", "-", "-", "-", "o", "-", "-", "-", "-", "-", "o"]]

    def reset(self):
        self.board = self.generateEmptyBoard()
        self.phase = 0

    def place(self, x, y, color):
        self.board[y][x] = color

    def take(self, x, y):
        self.board[y][x] = "o"

    def update(self):



        if self.playerTurn == "w":
            self.playerTurn = "b"
        elif self.playerTurn == "b":
            self.playerTurn = "w"
