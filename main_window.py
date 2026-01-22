"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 22/01/2026.
    Version: 1.1
    Copyright © 2026 Maciej Nalewajka. All rights reserved.
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
        self.f3x3Button = QtWidgets.QPushButton(self)
        self.f4x4Button = QtWidgets.QPushButton(self)
        self.f5x5Button = QtWidgets.QPushButton(self)
        self.f6x6Button = QtWidgets.QPushButton(self)
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
        
        self.f3x3Button.setObjectName("3x3")
        self.f3x3Button.setGeometry(190, 220, 90, 50)
        self.f3x3Button.setText("3x3")
        self.f3x3Button.setStyleSheet(self.getSelectedSizeButtonStyle())
        self.f3x3Button.setCursor(Qt.PointingHandCursor)

        self.f4x4Button.setObjectName("4x4")
        self.f4x4Button.setGeometry(300, 220, 90, 50)
        self.f4x4Button.setText("4x4")
        self.f4x4Button.setStyleSheet(self.getNotSelectedSizeButtonStyle())
        self.f4x4Button.setCursor(Qt.PointingHandCursor)

        self.f5x5Button.setObjectName("5x5")
        self.f5x5Button.setGeometry(410, 220, 90, 50)
        self.f5x5Button.setText("5x5")
        self.f5x5Button.setStyleSheet(self.getNotSelectedSizeButtonStyle())
        self.f5x5Button.setCursor(Qt.PointingHandCursor)

        self.f6x6Button.setObjectName("6x6")
        self.f6x6Button.setGeometry(520, 220, 90, 50)
        self.f6x6Button.setText("6x6")
        self.f6x6Button.setStyleSheet(self.getNotSelectedSizeButtonStyle())
        self.f6x6Button.setCursor(Qt.PointingHandCursor)

        self.exitButton.setObjectName("Exit Button")
        self.exitButton.setGeometry(300, 420, 200, 80)
        self.exitButton.setText("Exit")
        self.exitButton.setStyleSheet(self.__getExitButtonStyle())
        self.exitButton.setCursor(Qt.PointingHandCursor)

        self.player1Name.setGeometry(190, 150, 200, 40)
        self.player2Name.setGeometry(410, 150, 200, 40)
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
    
    def getNotSelectedSizeButtonStyle(self):
        styleSheet = """QPushButton {background-color: #A6CDC6; color: black; font-size: 20px; font-weight: bold; border-radius: 10px;}
        QPushButton:hover {background-color: #5F8B4C; border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet
    
    def getSelectedSizeButtonStyle(self):
        styleSheet = """QPushButton {background-color: #5F8B4C; color: black; font-size: 20px; font-weight: bold; border-radius: 10px;
        border-color: black; border-style: solid; border-width: 2px;}"""
        return styleSheet