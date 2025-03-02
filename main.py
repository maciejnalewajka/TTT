"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 02/03/2025.
    Version: 1.004
    Copyright © 2025 Maciej Nalewajka. All rights reserved.

    Simply example of Tic-Tac-Toe game.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from game_window import GameWindow
from main_window import MainWindow
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class TTTWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\icon.jpg"))
        # self.startMainWigdet()
        self.startGameWigdet()            #to remove

    def startMainWigdet(self):
        self.mainWindow = MainWindow()
        self.setCentralWidget(self.mainWindow)
        # self.mainWindow.playButton.clicked.connect(self.startGameWigdet)             #need to create button
        self.show()

    def startGameWigdet(self):
        self.gameWindow = GameWindow()
        self.setCentralWidget(self.gameWindow)
        self.gameWindow.backToMainButton.clicked.connect(self.startMainWigdet)
        self.gameWindow.newGameButton.clicked.connect(self.startGameWigdet)
        self.show()



def main():
    app = QApplication(sys.argv)
    win = TTTWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()