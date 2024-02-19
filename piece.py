from vars import *

class Piece:

    def __init__(self, row, col, color, king = False):
        self.row = row
        self.col = col
        self.color = color
        self.king = king
        self.legal = []
        self.right = size - 1 - self.col # Space left until right limit
        self.down = size - 1 - self.row # Space left until bottom limit
        self.catch = False # To check if there is a piece to catch or not
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.right = size - 1 - col
        self.down = size - 1 - row
        # If the piece reaches the last row, it becomes a king
        if row == 0 and self.color == WHITE:
            self.king = True
        if row == 7 and self.color == BLACK:
            self.king = True

    # Function to check the legal moves (later we have to deal with occupied positions, and capturing pieces)
    def legal_positions(self):
        if not self.king and self.color == BLACK and self.row < 7:
            if self.right == 0:
                self.legal = [(self.row + 1, self.col), (self.row + 1, self.col - 1)]
            elif self.col == 0:
                self.legal = [(self.row + 1, self.col), (self.row + 1, self.col + 1)]
            else:
                self.legal = [(self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col - 1)]

        if not self.king and self.color == WHITE and self.row:
            if self.right == 0:
                self.legal = [(self.row - 1, self.col), (self.row - 1, self.col - 1)]
            elif self.col == 0:
                self.legal = [(self.row - 1, self.col), (self.row - 1, self.col + 1)]
            else:
                self.legal = [(self.row - 1, self.col), (self.row - 1, self.col + 1), (self.row - 1, self.col - 1)]

        if self.king:
            self.legal = []

            # Moves to the right
            if self.right:
                for col in range(1, self.right + 1):
                    self.legal += [(self.row, self.col + col)]
            
            # Moves to the left
            if self.col:
                for col in range(1, self.col + 1):
                    self.legal += [(self.row, self.col - col)]

            # Moves upwards
            if self.row:
                for row in range(1, self.row + 1):
                    self.legal += [(self.row - row, self.col)]    

            # Moves downwards
            if self.down:
                for row in range(1, self.down + 1):
                    self.legal += [(self.row + row, self.col)]

            # Moves diagonally
                # up right
            if self.row and self.right:
                for row in range(1, self.row + 1):
                    for col in range(1, self.right + 1):
                        self.legal += [(self.row - row, self.col + col)]
            
                # down right
            if self.down and self.right:
                for row in range(1, self.down + 1):
                    for col in range(1, self.right + 1):
                        self.legal += [(self.row + row, self.col + col)]

                # up left
            if self.row and self.col:
                for row in range(1, self.row + 1):
                    for col in range(1, self.col + 1):
                        self.legal += [(self.row - row, self.col - col)]

                # down left
            if self.down and self.col:
                for row in range(1, self.down + 1):
                    for col in range(1, self.col + 1):
                        self.legal += [(self.row + row, self.col - col)]
    """
    # Function to check if the position is free
    def check_position(self):
        Board.occupied()
        for i in range(len(self.legal)):
            if self.legal[i] in taken:
                self.legal.pop(i)
    """

'''

# Lists to hold the pieces for each player
all_pieces_white = []
all_pieces_black = []

# Initial pieces for WHITE
for row in [5, 6, 7]:
    for col in range(8):
        if (row == 6 and col in [0, 7]) or (row == 5 and col in [0, 1, 6, 7]):
            continue
        else:
            piece = Piece(row, col, WHITE)
            all_pieces_white.append(piece)

# Initial pieces for BLACK
for row in range(3):
    for col in range(8):
        if (row == 1 and col in [0, 7]) or (row == 2 and col in [0, 1, 6, 7]):
            continue
        else:
            piece = Piece(row, col, BLACK)
            all_pieces_black.append(piece)
'''

