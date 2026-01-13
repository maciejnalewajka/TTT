"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 26/03/2025.
    Version: 1.005
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.mainLabel = QtWidgets.QLabel(self)
        self.playButton = QtWidgets.QPushButton(self)
        self.exitButton = QtWidgets.QPushButton(self)
        self.player1Name = QtWidgets.QLineEdit(self)
        self.player2Name = QtWidgets.QLineEdit(self)
        
        self.__initMainView()

    def __initMainView(self):
        self.mainLabel.setObjectName("Main Label")
        self.mainLabel.setGeometry(275, 10, 200, 50)
        self.mainLabel.setText("Tic-Tac-Toe")
        self.mainLabel.setStyleSheet(self.__getMainLabelStyle())
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.adjustSize()

        self.playButton.setObjectName("Play Button")
        self.playButton.setGeometry(300, 300, 200, 80)
        self.playButton.setText("Play")
        self.playButton.setStyleSheet(self.__getPlayButtonStyle())
        self.playButton.setCursor(Qt.PointingHandCursor)
        self.exitButton.setObjectName("Exit Button")
        self.exitButton.setGeometry(300, 420, 200, 80)
        self.exitButton.setText("Exit")
        self.exitButton.setStyleSheet(self.__getExitButtonStyle())
        self.exitButton.setCursor(Qt.PointingHandCursor)

        self.player1Name.setGeometry(300, 150, 200, 40)
        self.player2Name.setGeometry(300, 210, 200, 40)
        self.player1Name.setPlaceholderText("Player 1")
        self.player2Name.setPlaceholderText("Player 2")
        self.player1Name.setStyleSheet(self.__getPlayerNameLabelStyle())
        self.player2Name.setStyleSheet(self.__getPlayerNameLabelStyle())
        
    def __getMainLabelStyle(self):
        styleSheet = """QLabel {background-color: #FBF5DD; color: black; font-size: 40px; font-weight: bold; border-radius: 10px;
        padding: 10px;}"""
        return styleSheet

    def __getPlayButtonStyle(self):
        styleSheet = """QPushButton {background-color: #A6CDC6; color: black; font-size: 20px; font-weight: bold; border-radius: 10px;}
        QPushButton:hover {background-color: #5F8B4C; border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet
    
    def __getExitButtonStyle(self):
        styleSheet = """QPushButton {background-color: #A6CDC6; color: black; font-size: 20px; font-weight: bold; border-radius: 10px;}
        QPushButton:hover {background-color: #5F8B4C; border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet
    
    def __getPlayerNameLabelStyle(self):
        styleSheet = """QLineEdit {background-color: #FBF5DD; color: black; font-size: 20px; font-weight: bold; border-radius: 10px;
        border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet