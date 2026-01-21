"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 21/01/2026.
    Version: 1.008
    Copyright © 2026 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
import math as Math
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class Game():

    def __init__(self, scorePlayer1Label, scorePlayer2Label):
        super(Game, self).__init__()
        self.scorePlayer1Label = scorePlayer1Label
        self.scorePlayer2Label = scorePlayer2Label
        self.__pixmap_O = QPixmap("IMAGE\\O.png")
        self.__pixmap_X = QPixmap("IMAGE\\X.png")
        self.__pixmap_empty = QPixmap("IMAGE\\empty.png")
        self.__pixType = "X"
        self.__scorePlayer1 = 0
        self.__scorePlayer2 = 0
        self.listOfButtons = []
        self.buttonSize = 0
        self.Xlist = []
        self.Olist = []

    def startGame(self, listOfButtons, buttonSize):    #Function to start game
        self.listOfButtons = listOfButtons
        self.buttonSize = buttonSize
        self.__initGameButtons()

    def __initGameButtons(self):       #Function to create buttons with chars
        buttonsDict = {index: value for index, value in enumerate(self.listOfButtons)}      #Create dictionary with buttons and indexes of buttons  
        for idx, button in enumerate(buttonsDict.values()):
            button.clicked.connect(lambda checked, idx=idx: self.__setIcon(self.listOfButtons[idx], idx))               #Connect buttons with function
            button.setIconSize(QSize(self.buttonSize-5, self.buttonSize-5))                         #Set size of icon to 100x100

    def __setIcon(self, button, idx):    #Function to set icon of button
        if(button.icon().isNull()):
            match(self.__pixType):
                case "X":
                    button.setIcon(QIcon(self.__pixmap_X))      #Set icon of button to X icon
                    self.Xlist.append(idx)
                case "O":
                    button.setIcon(QIcon(self.__pixmap_O))      #Set icon of button to O icon
                    self.Olist.append(idx)
                case _:
                    button.setIcon(QIcon(self.__pixmap_empty))      #Set icon of button to empty icon
            self.__whoWin()
            self.__pixTypeUpdate()

    def __pixTypeUpdate(self):    #Function to update pixType
        match(self.__pixType):
            case "X":
                self.__pixType = "O"
            case "O":
                self.__pixType = "X"
    
    def newGame(self):    #Function to reset game
        for button in self.listOfButtons:
            button.setIcon(QIcon(self.__pixmap_empty))      #Set icon of button to empty icon
        self.__scorePlayer1 = 0
        self.__scorePlayer2 = 0
        self.__pixType = "X"
        self.Xlist, self.Olist = [], []

    def __whoWin(self):
        rowSize = int(Math.sqrt(len(self.listOfButtons)))
        if self.__checkRows(rowSize) == 1 or self.__checkColumns(rowSize) == 1 or self.__checkDiagonals(rowSize) == 1:
            self.__scorePlayer1 += 1
            self.scorePlayer1Label.setText(str(self.__scorePlayer1))
        elif self.__checkRows(rowSize) == 2 or self.__checkColumns(rowSize) == 2 or self.__checkDiagonals(rowSize) == 2:
            self.__scorePlayer2 += 1
            self.scorePlayer2Label.setText(str(self.__scorePlayer2))

    def __checkRows(self, rowSize):
        for i in range(0, len(self.listOfButtons), rowSize):
            winX = True
            winO = True
            for j in range(0, rowSize):
                winX = winX and (i+j in self.Xlist)
                winO = winO and (i+j in self.Olist)
            if winX == True:
                return 1
            if winO == True:
                return 2
        return 0
    
    def __checkColumns(self, rowSize):
        for i in range(0, rowSize):
            winX = True
            winO = True
            for j in range(0, len(self.listOfButtons), rowSize):
                winX = winX and (i+j in self.Xlist)
                winO = winO and (i+j in self.Olist)
            if winX == True:
                return 1
            if winO == True:
                return 2
        return 0
    
    def __checkDiagonals(self, rowSize):
        winX = True
        winO = True
        for i in range(0, len(self.listOfButtons), rowSize+1):
            winX = winX and (i in self.Xlist)
            winO = winO and (i in self.Olist)
        if winX == True:
            return 1
        if winO == True:
            return 2

        winX = True
        winO = True
        for i in range(rowSize-1, len(self.listOfButtons)-1, rowSize-1):
            winX = winX and (i in self.Xlist)
            winO = winO and (i in self.Olist)
        if winX == True:
            return 1
        if winO == True:
            return 2
        return 0