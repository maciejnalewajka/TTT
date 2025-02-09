"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.

    Simply example of Tic-Tac-Toe game.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

import random as r

class TTT:

    def __init__(self, player1 = "Player1", player2 = "Player2"):
        self.player1 = player1
        self.player2 = player2
        self.board = self.initBoard()
        self.char1 = 'x'
        self.char2 = 'o'

    def __str__(self):
        return """Tic-Tac-Toe Class"""

    def initBoard(self):
        l = [[[],[],[]],[[],[],[]],[[],[],[]]]
        return l

    def show(self):
        for i in range(0, 3):
            print(self.board[i])
        print("")


    def isEmpty(self):
        k = True
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] != []:
                    k = False
                    break
        return k

    def isWin(self):
        p = self.isEmpty()
        if p == True: return False
        for i in self.board:
            if i[0] != [] and i[0] == i[1] == i[2]:
                return True
        for i in range(0, 3):
            if self.board[0][i] != [] and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if self.board[1][1] != []:
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
            if self.board[2][0] == self.board[1][1] == self.board[0][2]:
                return True
        return False

    def char(self, z):
        x = self.random_position()
        y = self.random_position()
        if self.board[x][y] != []: return False
        self.board[x][y] = z
        return True

    def random_position(self):
        return r.randint(0, 2)

    def isTie(self):
        for i in self.board:
            for j in i:
                if j == []:
                    return False
        print("TIE")
        return True

    def game_main(self):
        print(self.__str__())
        print(self.player1 + " vs " + self.player2 + "\n")
        p = self.isWin()
        while p == False:
            self.char(self.char1)
            p = self.isWin()
            self.show()
            if self.isTie(): break
            self.char(self.char2)
            p = self.isWin()
            self.show()
            if self.isTie(): break
        print("Game Over")