"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 20/02/2025.
    Version: 1.001
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from functools import partial

class TTTWindow(QMainWindow):

    def __init__(self):
        super(TTTWindow, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Tic-Tac-Toe")
        self.initUi()

    def initUi(self):
        self.__initCharButtons()


    def __btnClick(self, button):
        pass
        # button do something
    
    def update(self):
        pass
        # update elements

    def __initCharButtons(self, sizeOfboard):
        listOfButtons = []
        for i in range(9):
            self.charButton = QtWidgets.QPushButton(self)
            listOfButtons.append(self.charButton)
            listOfButtons[i].setGeometry((i%3)*101, (i//3)*101, 100, 100)       #Size and position of char buttons
            f_btnClick = partial(self.__btnClick, listOfButtons[i])
            listOfButtons[i].clicked.connect(f_btnClick)