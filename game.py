"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 01/03/2025.
    Version: 1.001
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class Game():

    def __init__(self):
        self.listOfButtons = []
        self.__pixType = ""

        self.pixmap_O = QPixmap("IMAGE\O.jpg")
        self.pixmap_X = QPixmap("IMAGE\X.jpg")
        self.pixmap_empty = QPixmap("IMAGE\empty.jpg")
        self.pixmap_X = QPixmap("IMAGE\X.jpg")


    def __pixTypeUpdate(self):
        match(self.__pixType):
            case "X":
                self.__pixType = "O"
            case "O":
                self.__pixType = "X"
    
    def but(self, button):
        match(self.__pixType):
            case "X":
                button.setIcon(QIcon(self.pixmap_X))      #Set icon of button to X icon
            case "O":
                button.setIcon(QIcon(self.pixmap_O))      #Set icon of button to O icon
            case _:
                button.setIcon(QIcon(self.pixmap_empty))      #Set icon of button to empty icon
        self.__pixTypeUpdate()