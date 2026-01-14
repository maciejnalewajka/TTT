"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 06/03/2025.
    Version: 1.004
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
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
        self.__setInitPixType("X")
        self.__scorePlayer1 = 0
        self.__scorePlayer2 = 0
        self.__initScores()

    def initGameButtons(self, listOfButtons, buttonSize):       #Function to create buttons with chars
        buttonsDict = {index: value for index, value in enumerate(listOfButtons)}      #Create dictionary with buttons and indexes of buttons  
        for idx, button in enumerate(buttonsDict.values()):
            button.clicked.connect(lambda checked, idx=idx: self.__but(listOfButtons[idx]))               #Connect buttons with function
            # self.__but(listOfButtons[idx])                                #Set icon of button to empty icon 
            button.setIconSize(QSize(buttonSize-5, buttonSize-5))                         #Set size of icon to 100x100

    def __setInitPixType(self, pixType):     #Function to set initial pixType
        self.__pixType = pixType

    def __pixTypeUpdate(self):    #Function to update pixType
        match(self.__pixType):
            case "X":
                self.__pixType = "O"
            case "O":
                self.__pixType = "X"
    
    def __but(self, button):    #Function to set icon of button
        if(button.icon().isNull()):
            match(self.__pixType):
                case "X":
                    button.setIcon(QIcon(self.__pixmap_X))      #Set icon of button to X icon
                case "O":
                    button.setIcon(QIcon(self.__pixmap_O))      #Set icon of button to O icon
                case _:
                    button.setIcon(QIcon(self.__pixmap_empty))      #Set icon of button to empty icon
            self.__pixTypeUpdate()

    def __initScores(self):    #Function to init scores
        self.__scorePlayer1 = 0
        self.__scorePlayer2 = 0

    def getScores(self):    #Function to get scores
        return self.__scorePlayer1, self.__scorePlayer2

# TODO: Add function to check win condition
# TODO: Add function to reset game
# TODO: Add scoreboard functionality