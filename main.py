"""----------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 21/01/2026.
    Version: 1.008
    Copyright © 2026 Maciej Nalewajka. All rights reserved.
    Used color palette:
    https://colorhunt.co/palette/fbf5dda6cdc616404ddda853, https://colorhunt.co/palette/5f8b4cffddabff9a9a945034

    Simply example of Tic-Tac-Toe game.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from GameWindow import GameWindow
from Main_window import MainWindow
"""------------------------------------------------------------IMPORTS------------------------------------------------------------------------------"""


class TTTMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowTitle("Tic-Tac-Toe")
        self.setWindowIcon(QIcon("ICON\\icon.jpg"))
        self.setStyleSheet("background-color: #FBF5DD;")
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
        self.show()

def main():
    app = QApplication(sys.argv)
    win = TTTMainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()