"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 28/02/2025.
    Version: 1.002
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from functools import partial

class TTTWindow(QMainWindow):

    def __init__(self):
        super(TTTWindow, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))
        self.initUi()

    def initUi(self):
        self.__initCharButtons(3)


    def __btnClick(self, button):
        pass
        # button do something
    
    def update(self):
        pass
        # update elements

    def __initCharButtons(self, sizeOfboard):
        listOfButtons = []
        for i in range(sizeOfboard*sizeOfboard):
            self.charButton = QtWidgets.QPushButton(self)
            listOfButtons.append(self.charButton)
            listOfButtons[i].setGeometry((i%sizeOfboard)*101, (i//sizeOfboard)*101, 100, 100)       #Size and position of char buttons
            listOfButtons[i].clicked.connect(lambda: self.__btnClick(listOfButtons[i]))