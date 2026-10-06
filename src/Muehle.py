import pygame


class Muehle:
    def __init__(self):
        self.board = self.generateEmptyBoard()

        self.phase = 0
        self.playerTurn = "w"

        self.playerPieceCounter = [0, 0]
        self.selectedPiece = [-1, -1]
        self.takeMove = False

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

        self.playerPieceCounter = [0, 0]
        self.selectedPiece = [-1, -1]
        self.takeMove = False

    def place(self, x, y, color):
        self.board[y][x] = color

    def placeCurrentPlayer(self, x, y):
        self.place(x, y, self.playerTurn)
        if self.playerTurn == "w":
            self.playerPieceCounter[0] += 1
        else:
            self.playerPieceCounter[1] += 1

    def take(self, x, y):
        self.board[y][x] = "o"

    def toggleSelect(self, x, y):
        if self.board[y][x] == "w":
            if self.selectedPiece != [-1, -1]:
                self.board[self.selectedPiece[1]][self.selectedPiece[0]] = "w"
            self.board[y][x] = "ws"
            self.selectedPiece = [x, y]
        elif self.board[y][x] == "b":
            if self.selectedPiece != [-1, -1]:
                self.board[self.selectedPiece[1]][self.selectedPiece[0]] = "b"
            self.board[y][x] = "bs"
            self.selectedPiece = [x, y]
        elif self.board[y][x] == "ws":
            self.board[y][x] = "w"
            self.selectedPiece = [-1, -1]
        elif self.board[y][x] == "bs":
            self.board[y][x] = "b"
            self.selectedPiece = [-1, -1]

    def swap(self, x, y):
        if self.selectedPiece != [-1, -1]:
            temp = self.board[y][x]
            self.board[y][x] = self.board[self.selectedPiece[1]][self.selectedPiece[0]].replace("s", "")
            self.board[self.selectedPiece[1]][self.selectedPiece[0]] = temp
            self.selectedPiece = [-1, -1]

    def checkSwap(self, x, y):
        if self.playerPieceCounter[0] == 3 and self.playerTurn == "w" or self.playerPieceCounter[1] == 3 and self.playerTurn == "b":
            return True

        return True

    def canTake(self, x, y):
        curX = x
        curY = y

        count = 1
        while self.board[y][curX] != "" and curX+1 <= 12:
            curX += 1
            if self.board[y][curX] == self.board[y][x]:
                count += 1

        while self.board[y][curX] != "" and curX-1 >= 0:
            curX -= 1
            if self.board[y][curX] == self.board[y][x]:
                count += 1

        if count == 3:
            return True

        count = 1
        while self.board[curY][x] != "" and curY + 1 <= 12:
            curY += 1
            if self.board[curY][x] == self.board[y][x]:
                count += 1

        while self.board[curY][x] != "" and curY - 1 >= 0:
            curY -= 1
            if self.board[curY][x] == self.board[y][x]:
                count += 1

        return count == 3

    def togglePlayerTurn(self):
        if self.playerTurn == "w":
            self.playerTurn = "b"
        elif self.playerTurn == "b":
            self.playerTurn = "w"

    def update(self, x, y):
        if self.takeMove:
            self.take(x, y)
            self.takeMove = False
            self.togglePlayerTurn()
        else:
            match self.phase:
                case 0: # place
                    if self.board[y][x] == "o":
                        self.placeCurrentPlayer(x, y)

                        self.togglePlayerTurn()
                        if self.canTake(x, y):
                            self.takeMove = True
                        if self.playerPieceCounter == [9, 9]:
                            self.phase = 1
                case 1: # move
                    if self.board[y][x] in ["w", "ws"] and self.playerTurn == "w":
                        self.toggleSelect(x, y)
                    elif self.board[y][x] in ["b", "bs"] and self.playerTurn == "b":
                        self.toggleSelect(x, y)
                    elif self.board[y][x] == "o" and self.selectedPiece != [-1, -1] and self.checkSwap(x, y):
                        self.swap(x, y)
                        if not self.canTake(x, y):
                            self.togglePlayerTurn()
                        else:
                            self.takeMove = True


