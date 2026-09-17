import pygame


class Muehle:
    def __init__(self):
        self.board = self.generateEmptyBoard()

        self.phase = 0
        self.playerTurn = "w"

        self.placeCounter = 0

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
        self.playerTurn = "w"

        self.placeCounter = 0

    def place(self, x, y, color):
        self.board[y][x] = color

    def placeCurrentPlayer(self, x, y):
        self.place(x, y, self.playerTurn)

    def take(self, x, y):
        self.board[y][x] = "o"

    def togglePlayerTurn(self):
        if self.playerTurn == "w":
            self.playerTurn = "b"
        elif self.playerTurn == "b":
            self.playerTurn = "w"

    def update(self, x, y):
        match self.phase:
            case 0: # place
                if self.board[y][x] == "o":
                    self.placeCurrentPlayer(x, y)

                    self.togglePlayerTurn()
                    self.placeCounter += 1
                    if self.placeCounter == 18:
                        self.phase = 1
            case 1: # move
                pass
