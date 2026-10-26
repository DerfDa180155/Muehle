import pygame


class Muehle:
    def __init__(self):
        self.board = self.generateEmptyBoard()

        self.phase = 0
        self.playerTurn = "w"

        self.playerPieceCounterTotal = [0, 0]
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

        self.playerPieceCounterTotal = [0, 0]
        self.playerPieceCounter = [0, 0]
        self.selectedPiece = [-1, -1]
        self.takeMove = False

    def place(self, x, y, color):
        self.board[y][x] = color

    def placeCurrentPlayer(self, x, y):
        self.place(x, y, self.playerTurn)
        if self.playerTurn == "w":
            self.playerPieceCounter[0] += 1
            self.playerPieceCounterTotal[0] += 1
        else:
            self.playerPieceCounter[1] += 1
            self.playerPieceCounterTotal[1] += 1

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
        if self.board[y][x] != "o" or self.phase == 0:
            return False

        if self.playerPieceCounter[0] == 3 and self.playerTurn == "w" or self.playerPieceCounter[1] == 3 and self.playerTurn == "b":
            return True

        curX = self.selectedPiece[0]
        curY = self.selectedPiece[1]

        check = False
        if x == curX:
            while not check and curY >= 0:
                curY -= 1
                if self.board[curY][x] == "o":
                    return True
            curY = self.selectedPiece[1]
            while not check and curY <= 12:
                curY += 1
                if self.board[curY][x] == "o":
                    return True
        elif y == curY:
            while not check and curX >= 0:
                curX -= 1
                if self.board[y][curX] == "o":
                    return True
            curX = self.selectedPiece[0]
            while not check and curX <= 12:
                curX += 1
                if self.board[y][curX] == "o":
                    return True
        return False

    def canTake(self, x, y):
        curX = x
        curY = y

        count = 1
        while self.board[y][curX] != "" and curX+1 <= 12:
            curX += 1
            if self.board[y][curX] == self.board[y][x]:
                count += 1

        curX = x
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

        curY = y
        while self.board[curY][x] != "" and curY - 1 >= 0:
            curY -= 1
            if self.board[curY][x] == self.board[y][x]:
                count += 1

        return count == 3

    def canTakeAnyPiece(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.playerTurn == "w" and self.board[y][x] == "b" or self.playerTurn == "b" and self.board[y][x] == "w":
                    if not self.canTake(x, y):
                        return True

        return False

    def togglePlayerTurn(self):
        if self.playerTurn == "w":
            self.playerTurn = "b"
        elif self.playerTurn == "b":
            self.playerTurn = "w"

    def update(self, x, y):
        if self.takeMove:
            if self.board[y][x] not in [self.playerTurn, "o"] and not self.canTake(x, y):
                self.take(x, y)
                self.takeMove = False
                self.togglePlayerTurn()
                if self.playerTurn == "w":
                    self.playerPieceCounter[0] -= 1
                    if self.playerPieceCounter[0] == 2 and self.phase == 2:
                        self.phase = 3
                elif self.playerTurn == "b":
                    self.playerPieceCounter[1] -= 1
                    if self.playerPieceCounter[1] == 2 and self.phase == 2:
                        self.phase = 3
        else:
            match self.phase:
                case 0: # place
                    if self.board[y][x] == "o":
                        self.placeCurrentPlayer(x, y)

                        if self.canTake(x, y) and self.canTakeAnyPiece():
                            self.takeMove = True
                        else:
                            self.togglePlayerTurn()

                        if self.playerPieceCounterTotal == [9, 9]:
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
                        elif self.canTakeAnyPiece():
                            self.takeMove = True


