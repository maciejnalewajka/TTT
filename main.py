"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 02/03/2025.
    Version: 1.003
    Copyright © 2025 Maciej Nalewajka. All rights reserved.

    Simply example of Tic-Tac-Toe game.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window import MainWindow
from game_window import GameWindow
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class TTTWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))
        # self.__startMainWigdet()
        self.__startGameWigdet()            #to remove

    def __startMainWigdet(self):
        self.mainWindow = MainWindow(self)
        self.setCentralWidget(self.mainWindow)
        # self.mainWindow.playButton.clicked.connect(self.__startGameWigdet)             #need to create button
        self.show()

    def __startGameWigdet(self):
        self.gameWindow = GameWindow(self)
        self.setCentralWidget(self.gameWindow)
        # self.gameWindow.backToMainButton.clicked.connect(self.__startMainWigdet)      #need to create button
        # self.gameWindow.newGameButton.clicked.connect(self.__startGameWigdet)         #need to create button
        self.show()



def main():
    app = QApplication(sys.argv)
    win = TTTWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()