"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 01/03/2025.
    Version: 1.003
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from game import Game

class TTTWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        print(type(self))
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))
        self.boardSize = 3
        self.listOfButtons = []
        self.game = Game()
        self.__initUi()

    def __initUi(self):
        #TODO: Init main view of game
        self.__initCharButtons(self.boardSize)
        

    def __btnClick(self, idx):
        self.game.but(self.listOfButtons[idx])

    def __initCharButtons(self, sizeOfboard):       #Function to create buttons with chars
        for i in range(0, sizeOfboard*sizeOfboard):
            self.charButton = QtWidgets.QPushButton(self)
            self.charButton.setObjectName("button " + str(i))
            self.listOfButtons.append(self.charButton)
            self.listOfButtons[i].setGeometry((i%sizeOfboard)*105, (i//sizeOfboard)*105, 100, 100)       #Size and position of char buttons

        buttonsDict = {index: value for index, value in enumerate(self.listOfButtons)}      #Create dictionary with buttons and indexes of buttons  
        for idx, button in enumerate(buttonsDict.values()):
            button.clicked.connect(lambda checked, idx=idx: self.__btnClick(idx))               #Connect buttons with function
            self.game.but(self.listOfButtons[idx])                                #Set icon of button to empty icon 
            button.setIconSize(QSize(100, 100))                         #Set size of icon to 100x100
        #TODO: Set game pixmap to not empty