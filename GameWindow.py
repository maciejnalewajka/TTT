"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 21/01/2026.
    Version: 1.008
    Copyright © 2026 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from Game import Game
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class GameWindow(QWidget):

    def __init__(self, player1Name, player2Name):
        super(GameWindow, self).__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        # Lock window to default size (uncomment/remove to allow resizing)
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("ICON\\icon.jpg"))

        self.newGameButton = QtWidgets.QPushButton(self)        #Button to start new game
        self.backToMainButton = QtWidgets.QPushButton(self)     #Button to back to main window
        self.player1Label = QtWidgets.QLabel(self)              #Label to show player1 name
        self.scorePlayer1Label = QtWidgets.QLabel(self)              #Label to show player1 score
        self.player2Label = QtWidgets.QLabel(self)              #Label to show player2 name
        self.scorePlayer2Label = QtWidgets.QLabel(self)              #Label to show player2 score
        self.vsLabel = QtWidgets.QLabel(self)              #Label to show player2 name
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.initPlayerName(player1Name, player2Name)
        self.listOfButtons = []
        self.game = Game(self.scorePlayer1Label, self.scorePlayer2Label)
        self.__initUi()

    def __initUi(self):    #Function to init UI
        self.__initVsLabel()
        self.__initPlayer1Label()
        self.__initScorePlayer1Label()
        self.__initPlayer2Label()
        self.__initScorePlayer2Label()
        self.__initNewGameButton()
        self.__initBackToMainButton()
        self.__initCharButtons(4)

    def __initCharButtons(self, buttonsInRow):       #Function to create buttons with chars
        buttonSize = 555//buttonsInRow
        for i in range(0, buttonsInRow*buttonsInRow):
            self.charButton = QtWidgets.QPushButton(self)
            self.charButton.setObjectName("Button " + str(i))
            self.charButton.setCursor(Qt.PointingHandCursor)
            self.listOfButtons.append(self.charButton)
            #Size and position of char buttons
            self.listOfButtons[i].setGeometry((i%buttonsInRow)*(buttonSize+5)+15, (i//buttonsInRow)*(buttonSize+5)+15, buttonSize, buttonSize)
            self.listOfButtons[i].setStyleSheet("background-color: #FFFFFF; border-radius: 5px; border-color: black; border-style: solid; border-width: 1px;")
        self.game.startGame(self.listOfButtons, buttonSize)
        self.listOfButtons = []

    def initPlayerName(self, player1, player2):
        if player1 == "":
            player1 = "Player 1"
        if player2 == "":
            player2 = "Player 2"
        self.player1Label.setText(player1)
        self.player2Label.setText(player2)

    def __initVsLabel(self):
        self.vsLabel.setObjectName("Label VS")
        self.vsLabel.setGeometry(610, 65, 170, 50)
        self.vsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vsLabel.setText("VS")
        self.vsLabel.setStyleSheet(self.__getvsLabelStyle())
        
    def __initPlayer1Label(self):
        self.player1Label.setObjectName("Label Player 1")
        self.player1Label.setGeometry(610, 15, 130, 50)
        self.player1Label.setStyleSheet(self.__getplayer1LabelStyle())
        self.player1Label.setAlignment(QtCore.Qt.AlignCenter)

    def __initScorePlayer1Label(self):
        self.scorePlayer1Label.setObjectName("Label Score Player 1")
        self.scorePlayer1Label.setGeometry(730, 15, 50, 50)
        self.scorePlayer1Label.setStyleSheet(self.__getscorePlayer1LabelStyle())
        self.scorePlayer1Label.setText("0")
        self.scorePlayer1Label.setAlignment(QtCore.Qt.AlignCenter)

    def __initPlayer2Label(self):
        self.player2Label.setObjectName("Label Player 2")
        self.player2Label.setGeometry(610, 115, 130, 50)
        self.player2Label.setStyleSheet(self.__getplayer2LabelStyle())
        self.player2Label.setAlignment(QtCore.Qt.AlignCenter)

    def __initScorePlayer2Label(self):
        self.scorePlayer2Label.setObjectName("Label Score Player 2")
        self.scorePlayer2Label.setGeometry(730, 115, 50, 50)
        self.scorePlayer2Label.setStyleSheet(self.__getscorePlayer2LabelStyle())
        self.scorePlayer2Label.setText("0")
        self.scorePlayer2Label.setAlignment(QtCore.Qt.AlignCenter)

    def __initNewGameButton(self):
        self.newGameButton.setObjectName("Button New Game")
        self.newGameButton.setGeometry(610, 200, 170, 50)
        self.newGameButton.setText("New Game")
        self.newGameButton.setStyleSheet(self.__getNewGameButtonStyle())
        self.newGameButton.clicked.connect(lambda: self.game.newGame())
        self.newGameButton.setCursor(Qt.PointingHandCursor)
    
    def __initBackToMainButton(self):
        self.backToMainButton.setObjectName("Button Back To Main")
        self.backToMainButton.setGeometry(610, 260, 170, 50)
        self.backToMainButton.setText("Main Menu")
        self.backToMainButton.setStyleSheet(self.__getbackToMainButtonStyle())
        self.backToMainButton.setCursor(Qt.PointingHandCursor)

    def __getplayer1LabelStyle(self):
        styleSheet = """background-color: #000000; color: white; font-size: 16px; font-weight: bold; border-top-left-radius: 10px;"""
        return styleSheet
    
    def __getscorePlayer1LabelStyle(self):
        styleSheet = """background-color: #000000; color: white; font-size: 16px; font-weight: bold; border-top-right-radius: 10px;"""
        return styleSheet
    
    def __getplayer2LabelStyle(self):
        styleSheet = """background-color: #000000; color: white; font-size: 16px; font-weight: bold; border-bottom-left-radius: 10px;"""
        return styleSheet

    def __getscorePlayer2LabelStyle(self):
        styleSheet = """background-color: #000000; color: white; font-size: 16px; font-weight: bold; border-bottom-right-radius: 10px;"""
        return styleSheet
    
    def __getvsLabelStyle(self):
        styleSheet = """background-color: #000000; color: white; font-size: 20px; font-weight: bold; padding-right: 50px;"""
        return styleSheet

    def __getNewGameButtonStyle(self):
        styleSheet = """QPushButton {background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;}
        QPushButton:hover {background-color: #5F8B4C; border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet
    
    def __getbackToMainButtonStyle(self):
        styleSheet = """QPushButton {background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;}
        QPushButton:hover {background-color: #5F8B4C; border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet