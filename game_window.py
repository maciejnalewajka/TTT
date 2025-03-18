"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 18/03/2025.
    Version: 1.007
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from game import Game

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class GameWindow(QWidget):

    def __init__(self, player1Name, player2Name):
        super(GameWindow, self).__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))

        self.newGameButton = QtWidgets.QPushButton(self)        #Button to start new game
        self.backToMainButton = QtWidgets.QPushButton(self)     #Button to back to main window
        self.player1Label = QtWidgets.QLabel(self)              #Label to show player1 name
        self.player2Label = QtWidgets.QLabel(self)              #Label to show player2 name
        self.vsLabel = QtWidgets.QLabel(self)              #Label to show player2 name
        self.player1Name = player1Name
        self.player2Name = player2Name

        self.listOfButtons = []
        self.game = Game()
        self.__initUi()

    def __initUi(self):    #Function to init UI
        self.player1Label.setObjectName("Label Player 1")
        self.player1Label.setGeometry(620, 15, 150, 50)
        self.player1Label.setText(self.player1Name)
        self.player1Label.setStyleSheet("background-color: #000000; color: white; font-size: 15px; font-weight: bold; border-top-left-radius: 10px; "
        "border-top-right-radius: 10px;")
        self.player1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.vsLabel.setObjectName("Label VS")
        self.vsLabel.setGeometry(620, 65, 150, 50)
        self.vsLabel.setText("VS")
        self.vsLabel.setStyleSheet("background-color: #000000; color: white; font-size: 25px; font-weight: bold;")
        self.vsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.player2Label.setObjectName("Label Player 2")
        self.player2Label.setGeometry(620, 115, 150, 50)
        self.player2Label.setText(self.player2Name)
        self.player2Label.setStyleSheet("background-color: #000000; color: white; font-size: 15px; font-weight: bold; border-bottom-left-radius: 10px; "
        "border-bottom-right-radius: 10px;")
        self.player2Label.setAlignment(QtCore.Qt.AlignCenter)

        self.newGameButton.setObjectName("Button New Game")
        self.newGameButton.setGeometry(620, 200, 150, 50)
        self.newGameButton.setText("New Game")
        self.newGameButton.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")
        self.backToMainButton.setObjectName("Button Back To Main")
        self.backToMainButton.setGeometry(620, 260, 150, 50)
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

