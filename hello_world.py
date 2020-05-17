import sys
from PyQt5.QtWidgets import (QMainWindow, QFrame, QWidget, QGridLayout, QPushButton, QApplication, QDesktopWidget)

class Chess(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Initiates application UI

        # self.chess_board = Board(self)
        # self.chess_board.start()

        chess_board_layout = QGridLayout()
        self.setLayout(chess_board_layout)

        board = [[[] for x in range(8)] for y in range(8)]
    
        # Setup board
        for x in range(8):
            for y in range(8):
                if x == 1:
                    board[x][y] = {"color":"White","piece":"Pawn"}
                if x == 6:
                    board[x][y] = {"color":"Black","piece":"Pawn"}
                if x == 0:
                    board[x][y] = {"color":"Blank","piece":"Blank"}
                if x == 7:
                    board[x][y] = {"color":"Blank","piece":"Blank"}
                if x > 1 and x < 6: 
                    board[x][y] = {"color":"Blank","piece":"Blank"}

        for x in range(8):
            for y in range(8):
                if board[x][y]['piece'] == 'Pawn':
                    button = QPushButton('Pawn')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Blank':
                    button = QPushButton('Blank')
                    chess_board_layout.addWidget(button, x, y)

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
    def turnEvent(self):
        # Call every time a move is made to refresh the board
        print("Test")


# Starts the application
if __name__ == '__main__':
    
    app = QApplication([])
    chess = Chess()    
    sys.exit(app.exec_())