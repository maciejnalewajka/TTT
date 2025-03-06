"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 06/03/2025.
    Version: 1.003
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.playButton = QtWidgets.QPushButton(self)
        self.exitButton = QtWidgets.QPushButton(self)

        self.player1Name = QtWidgets.QLineEdit(self)
        self.player2Name = QtWidgets.QLineEdit(self)
        

        self.__initMainView()

    def __initMainView(self):
        self.playButton.setObjectName("Play Button")
        self.playButton.setGeometry(300, 200, 200, 100)
        self.playButton.setText("Play")
        self.playButton.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")
        self.exitButton.setObjectName("Exit Button")
        self.exitButton.setGeometry(300, 350, 200, 100)
        self.exitButton.setText("Exit")
        self.exitButton.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px")

        self.player1Name.setGeometry(300, 100, 200, 50)
        self.player2Name.setGeometry(300, 150, 200, 50)
        self.player1Name.setPlaceholderText("Player 1")
        self.player2Name.setPlaceholderText("Player 2")
        self.player1Name.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")
        self.player2Name.setStyleSheet("background-color: #000000; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")