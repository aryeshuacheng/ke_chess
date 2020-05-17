import sys
from PyQt5.QtWidgets import (QMainWindow, QFrame, QWidget, QGridLayout, QPushButton, QApplication, QDesktopWidget)

class Chess(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Initiates application UI

        self.chess_board = Board(self)
        self.chess_board.start()

        chess_board_layout = QGridLayout()
        self.setLayout(chess_board_layout)

        # Setup board
        for x in range(9):
            for y in range(9):
                if x == 1:
                    chess_board_layout.addWidget(QPushButton("White Pawn"), x, y)
                if x > 1 and x < 7:
                    chess_board_layout.addWidget(QPushButton("Free Space"), x, y)
                if x == 7:
                    chess_board_layout.addWidget(QPushButton("Black Pawn"), x, y)

        self.resize(600, 600)
        self.center()
        self.setWindowTitle('Chess')        
        self.show()

    def center(self):
        # Centers window on screen
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)

class Board(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.initBoard()

    def initBoard(self):     
    # Initiates board
        self.board = []

    def start(self):
        # Starts game

        self.isStarted = True

# Starts the application
if __name__ == '__main__':
    
    app = QApplication([])
    chess = Chess()    
    sys.exit(app.exec_())