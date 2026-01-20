"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 19/01/2026.
    Version: 1.008
    Copyright © 2026 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
import math as Math
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class Game():

    def __init__(self):
        super(Game, self).__init__()
        self.__pixmap_O = QPixmap("IMAGE\\O.png")
        self.__pixmap_X = QPixmap("IMAGE\\X.png")
        self.__pixmap_empty = QPixmap("IMAGE\\empty.png")
        self.__pixType = "X"
        self.__scorePlayer1 = 0
        self.__scorePlayer2 = 0
        self.listOfButtons = []
        self.buttonSize = 0
        self.pixChecker = None

    def startGame(self, listOfButtons, buttonSize):    #Function to start game
        self.listOfButtons = listOfButtons
        self.buttonSize = buttonSize
        self.__initGameButtons()
        self.pixChecker = self.listOfButtons[0].icon().pixmap(self.buttonSize).toImage().format()

    def __initGameButtons(self):       #Function to create buttons with chars
        buttonsDict = {index: value for index, value in enumerate(self.listOfButtons)}      #Create dictionary with buttons and indexes of buttons  
        for idx, button in enumerate(buttonsDict.values()):
            button.clicked.connect(lambda checked, idx=idx: self.__setIcon(self.listOfButtons[idx]))               #Connect buttons with function
            button.setIconSize(QSize(self.buttonSize-5, self.buttonSize-5))                         #Set size of icon to 100x100

    def __setIcon(self, button):    #Function to set icon of button
        if(button.icon().isNull()):
            match(self.__pixType):
                case "X":
                    button.setIcon(QIcon(self.__pixmap_X))      #Set icon of button to X icon
                case "O":
                    button.setIcon(QIcon(self.__pixmap_O))      #Set icon of button to O icon
                case _:
                    button.setIcon(QIcon(self.__pixmap_empty))      #Set icon of button to empty icon
            if(self.__isWin()):
                print("Win")
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
        self.__pixType = "X"

    def __isWin(self):
        rowSize = int(Math.sqrt(len(self.listOfButtons)))
        if self.__pixType == "X":
            pixIcon = self.__pixmap_X
        if self.__pixType == "O":
            pixIcon = self.__pixmap_O
        win = 0
        for i in range(0, len(self.listOfButtons), rowSize):
            # Check rows
            if (self.listOfButtons[i].icon().pixmap(self.buttonSize).toImage().format() == \
                self.listOfButtons[i+1].icon().pixmap(self.buttonSize).toImage().format() == \
                self.listOfButtons[i+2].icon().pixmap(self.buttonSize).toImage().format() == \
                self.listOfButtons[i+3].icon().pixmap(self.buttonSize).toImage().format() == \
                pixIcon.toImage().format()):
                    return True
        # for i in range(0, , rowSize):
        #     if (self.listOfButtons[i].icon().pixmap(self.buttonSize).toImage().format() == \
        #         self.listOfButtons[i+rowSize].icon().pixmap(self.buttonSize).toImage().format() == \
        #         self.listOfButtons[i+(rowSize*2)].icon().pixmap(self.buttonSize).toImage().format() == \
        #         self.listOfButtons[i+(rowSize*3)].icon().pixmap(self.buttonSize).toImage().format() == \
        #         pixIcon.toImage().format()):
        #             print("Row win 2")
        #             return True
            

        # # Check columns
        # for i in range(3):
        #     if self.listOfButtons[i].icon().pixmap(self.buttonSize).toImage().format() != 0 and \
        #        self.listOfButtons[i].icon().pixmap(self.buttonSize).toImage().format() == \
        #        self.listOfButtons[i+3].icon().pixmap(self.buttonSize).toImage().format() == \
        #        self.listOfButtons[i+6].icon().pixmap(self.buttonSize).toImage().format():
        #         return True

        # # Check diagonals
        # if self.listOfButtons[0].icon().pixmap(self.buttonSize).toImage().format() != 0 and \
        #    self.listOfButtons[0].icon().pixmap(self.buttonSize).toImage().format() == \
        #    self.listOfButtons[4].icon().pixmap(self.buttonSize).toImage().format() == \
        #    self.listOfButtons[8].icon().pixmap(self.buttonSize).toImage().format():
        #     return True

        # if self.listOfButtons[2].icon().pixmap(self.buttonSize).toImage().format() != 0 and \
        #    self.listOfButtons[2].icon().pixmap(self.buttonSize).toImage().format() == \
        #    self.listOfButtons[4].icon().pixmap(self.buttonSize).toImage().format() == \
        #    self.listOfButtons[6].icon().pixmap(self.buttonSize).toImage().format():
        #     return True

        # return False