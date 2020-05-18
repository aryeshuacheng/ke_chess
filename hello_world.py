import sys
from PyQt5.QtWidgets import (QMainWindow, QFrame, QWidget, QGridLayout, QPushButton, QApplication, QDesktopWidget)

class Chess(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Initiates application UI

        chess_board_layout = QGridLayout()
        self.setLayout(chess_board_layout)

        board = [[[] for x in range(8)] for y in range(8)]
    
        # Setup board
        for x in range(8):
            for y in range(8):
                if x == 0 and y == 0:
                    board[x][y] = {"color":"White","piece":"Rook"}
                if x == 0 and y == 1:
                    board[x][y] = {"color":"White","piece":"Bishop"}
                if x == 0 and y == 2:
                    board[x][y] = {"color":"White","piece":"Knight"}
                if x == 0 and y == 3:
                    board[x][y] = {"color":"White","piece":"Queen"}
                if x == 0 and y == 4:
                    board[x][y] = {"color":"White","piece":"King"}
                if x == 0 and y == 5:
                    board[x][y] = {"color":"White","piece":"Bishop"}
                if x == 0 and y == 6:
                    board[x][y] = {"color":"White","piece":"Knight"}
                if x == 0 and y == 7:
                    board[x][y] = {"color":"White","piece":"Rook"}
                if x == 7 and y == 0:
                    board[x][y] = {"color":"Black","piece":"Rook"}
                if x == 7 and y == 1:
                    board[x][y] = {"color":"Black","piece":"Bishop"}
                if x == 7 and y == 2:
                    board[x][y] = {"color":"Black","piece":"Knight"}
                if x == 7 and y == 3:
                    board[x][y] = {"color":"Black","piece":"Queen"}
                if x == 7 and y == 4:
                    board[x][y] = {"color":"Black","piece":"King"}
                if x == 7 and y == 5:
                    board[x][y] = {"color":"Black","piece":"Bishop"}
                if x == 7 and y == 6:
                    board[x][y] = {"color":"Black","piece":"Knight"}
                if x == 7 and y == 7:
                    board[x][y] = {"color":"Black","piece":"Rook"}
                if x == 1:
                    board[x][y] = {"color":"White","piece":"Pawn"}
                if x == 6:
                    board[x][y] = {"color":"Black","piece":"Pawn"}
                if x > 1 and x < 6: 
                    board[x][y] = {"color":"Blank","piece":"Blank"}

        for x in range(8):
            for y in range(8):
                if board[x][y]['piece'] == 'Pawn':
                    button = QPushButton('Pawn ({},{})'.format(x,y), self)
                    chess_board_layout.addWidget(button, x, y)
                    button.clicked.connect(lambda ch, x=x,y=y:self.select_Pawn(x,y, board, chess_board_layout))
                if board[x][y]['piece'] == 'Blank':
                    button = QPushButton('Blank')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Rook':
                    button = QPushButton('Rook')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Bishop':
                    button = QPushButton('Bishop')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Rook':
                    button = QPushButton('Rook')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Queen':
                    button = QPushButton('Queen')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'King':
                    button = QPushButton('King')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Knight':
                    button = QPushButton('Knight')
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

    def select_Pawn(self, current_x, current_y, board, chess_board_layout):
        # Draw a new board with click event for moving piece
        print ("select_Pawn x:"+str(current_x))
        print ("select_Pawn y:"+str(current_y))
        self.drawAvailableMoves(current_x, current_y, board, chess_board_layout)
      


    def move_Pawn(self, new_x, new_y, current_x, current_y, board, chess_board_layout):
        board[new_x][new_y] = {"color":"White","piece":"Pawn"}
        board[current_x][current_y] = {"color":"Blank","piece":"Blank"}

        print(new_x)
        print(new_y)
        self.drawBoard(board,chess_board_layout)

       
    def drawAvailableMoves(self, current_x, current_y, board, chess_board_layout):
        # Called every time you make a move to update the board
        for x in range(8):
                for y in range(8):
                    button = QPushButton('Move Available ({},{})'.format(x,y), self)
                    chess_board_layout.addWidget(button, x, y)
                    button.clicked.connect(lambda ch, x=x,y=y:self.move_Pawn(x, y, current_x, current_y, board, chess_board_layout))
        
    def drawBoard(self, board, chess_board_layout):
        for x in range(8):
            for y in range(8):
                if board[x][y]['piece'] == 'Pawn':
                    button = QPushButton('Pawn', self)
                    chess_board_layout.addWidget(button, x, y)
                    button.clicked.connect(lambda: self.select_Pawn(x,y, board, chess_board_layout))
                if board[x][y]['piece'] == 'Blank':
                    button = QPushButton('Blank')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Rook':
                    button = QPushButton('Rook')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Bishop':
                    button = QPushButton('Bishop')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Rook':
                    button = QPushButton('Rook')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Queen':
                    button = QPushButton('Queen')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'King':
                    button = QPushButton('King')
                    chess_board_layout.addWidget(button, x, y)
                if board[x][y]['piece'] == 'Knight':
                    button = QPushButton('Knight')
                    chess_board_layout.addWidget(button, x, y)

# Starts the application
if __name__ == '__main__':
    
    app = QApplication([])
    chess = Chess()    
    sys.exit(app.exec_())