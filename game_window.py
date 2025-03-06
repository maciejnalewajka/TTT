"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 06/03/2025.
    Version: 1.006
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from game import Game

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class GameWindow(QWidget):

    def __init__(self):
        super(GameWindow, self).__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))

        self.newGameButton = QtWidgets.QPushButton(self)        #Button to start new game
        self.backToMainButton = QtWidgets.QPushButton(self)     #Button to back to main window

        self.listOfButtons = []
        self.game = Game()
        self.__initUi()

    def __initUi(self):    #Function to init UI
        self.newGameButton.setObjectName("Button New Game")
        self.newGameButton.setGeometry(620, 15, 150, 50)
        self.newGameButton.setText("New Game")
        self.newGameButton.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")
        self.backToMainButton.setObjectName("Button Back To Main")
        self.backToMainButton.setGeometry(620, 75, 150, 50)
        self.backToMainButton.setText("Back")
        self.backToMainButton.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")
        self.__initCharButtons(4)

    def __initCharButtons(self, buttonsInRow):       #Function to create buttons with chars
        buttonSize = 555//buttonsInRow
        for i in range(0, buttonsInRow*buttonsInRow):
            self.charButton = QtWidgets.QPushButton(self)
            self.charButton.setObjectName("Button " + str(i))
            self.listOfButtons.append(self.charButton)
            self.listOfButtons[i].setGeometry((i%buttonsInRow)*(buttonSize+5)+15, (i//buttonsInRow)*(buttonSize+5)+15, buttonSize, buttonSize)       #Size and position of char buttons
        self.game.initGameButtons(self.listOfButtons, buttonSize)

