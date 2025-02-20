"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 20/02/2025.
    Version: 1.001
    Copyright © 2025 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

class TTTWindow(QMainWindow):

    def __init__(self):
        super(TTTWindow, self).__init__()
        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle("Tic-Tac-Toe")
        # self.initUi()

    def initUi(self):
        pass
        # elements shown at start

    def btnClick(self, button):
        pass
        # button do something
    
    def update(self):
        pass
        # update elements