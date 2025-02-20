"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 20/02/2025.
    Version: 1.001
    Copyright © 2025 Maciej Nalewajka. All rights reserved.

    Simply example of Tic-Tac-Toe game.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

from ttt_gui import TTTWindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    win = TTTWindow()
    win.show()
    sys.exit(app.exec_())

main()