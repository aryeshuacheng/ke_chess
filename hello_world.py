from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
import sys, random

class Chess(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Initiates application UI

        self.chess_board = Board(self)
        self.setCentralWidget(self.chess_board)

        self.chess_board.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')        
        self.show()

    def center(self):
        # Centers window on screen
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)

class Board(QFrame):
    BoardWidth = 8
    BoardHeight = 8

    def __init__(self, parent):
        super().__init__(parent)
        
        self.initBoard()

    def initBoard(self):     
    # Initiates board
        self.board = []

    def start(self):
        # Starts game

        self.isStarted = True

        # I think we setup the initial configuration of the board here

        # Add White pieces here
        # {WhiteKingSideBishop: {position: [0,0]} i.e. poisiton: [x,y] on a 8x8 grid

        # Add Black pieces here

# Starts the application
if __name__ == '__main__':
    
    app = QApplication([])
    tetris = Chess()    
    sys.exit(app.exec_())