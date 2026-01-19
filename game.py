"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 19/01/2026.
    Version: 1.008
    Copyright © 2026 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
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

    def startGame(self, listOfButtons, buttonSize):    #Function to start game
        self.listOfButtons = listOfButtons
        self.buttonSize = buttonSize
        self.__initGameButtons()

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


# TODO: Add function to check win condition
# TODO: Add function to reset game
# TODO: Add scoreboard functionality