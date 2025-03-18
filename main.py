"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 18/03/2025.
    Version: 1.006
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
        self.startMainWidget()

    def startMainWidget(self):
        self.mainWindow = MainWindow()
        self.setCentralWidget(self.mainWindow)
        self.mainWindow.playButton.clicked.connect(lambda: self.startGameWidget(self.mainWindow.player1Name.text(), self.mainWindow.player2Name.text()))
        self.mainWindow.exitButton.clicked.connect(self.close)
        self.show()

    def startGameWidget(self, player1Name, player2Name):
        self.gameWindow = GameWindow(player1Name, player2Name)
        self.setCentralWidget(self.gameWindow)
        self.gameWindow.backToMainButton.clicked.connect(self.startMainWidget)
        self.gameWindow.newGameButton.clicked.connect(lambda: self.startGameWidget(player1Name, player2Name))
        self.show()



def main():
    app = QApplication(sys.argv)
    win = TTTWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()