__author__ = 'arpitgarg'

import numpy as np


class Board(object):
    nrow = 6  # Default row val
    ncol = 7  # Default col val
    moves = [0, 0, 1, 1, 2, 2, 3]  # Default moves val
    # Initializing board
    board = [['*'] * ncol] * nrow
    board = np.array(board)

    move_one = 0
    move_two = 0
    total_moves = 0

    def __init__(self, r, c, moves):
        self.nrow = r
        self.ncol = c
        self.moves = moves
        self.board = [['*'] * self.ncol] * self.nrow
        self.board = np.array(self.board)
        return

    # Function to play alternatively between two players
    def move(self):
        i = 0
        while i < len(self.moves):

            # Player 1
            player_one = self.moves[i]
            self.move_one += 1
            i += 1
            print "\nPlayer 1 puts in " + str(player_one+1)
            self.print_board(player_one, 'x')
            if self.move_one >= 4:
                if self.check_for_win('x'):
                    print "\nPlayer 1 won! " + str(self.move_one) + " pieces played."
                    return

            # Player 2
            player_two = self.moves[i]
            self.move_two += 2
            i += 1
            print "\nPlayer 2 puts in " + str(player_two+1)
            self.print_board(player_two, 'o')
            if self.move_two >= 4:
                if self.check_for_win('o'):
                    print "\nPlayer 2 won! " + str(self.move_two) + " pieces played."
                    return

        print "Draw"
        return

    # Function to put in the piece and print the board
    def print_board(self, move, player):

        for row in range(self.nrow - 1, -1, -1):
            if self.board[row, move] == '*':
                self.board[row, move] = player
                break
        print '\n'.join(' '.join(str(col) for col in row) for row in self.board)
        return

    # Function to check if after this move has the player won or not
    def check_for_win(self, player):

        for i in range(self.ncol):
            num = 0
            for j in range(self.nrow):
                if self.board[j, i] == player:
                    num += 1
                else:
                    num = 0

                if num >= 4:
                    return True

        # check for horizontal connections
        for i in range(self.nrow):
            num = 0
            for j in range(self.ncol):
                if self.board[i, j] == player:
                    num += 1
                else:
                    num = 0

                if num >= 4:
                    return True

        # check for negative increasing diagonals adding 1 to row and subtract 1 from col
        i = 0
        j = self.ncol - 4
        while i < self.nrow - 4 and j < self.ncol:
            index = (i, j)
            num = 0
            while index[0] < self.nrow and index[1] >= 0:
                if self.board[index] == player:
                    num += 1
                else:
                    num = 0

                if num >= 4:
                    return True

                index = (index[0] + 1, index[1] - 1)
            if i == 0:
                j += 1
            else:
                j = self.ncol - 1
                i += 1
        # check for positive increasing diagonals adding 1 to both row and col
        i = 0
        j = 0
        while i < self.nrow - 4 and j < self.ncol - 4:
            index = (i, j)
            num = 0
            while index[0] < self.nrow and index[1] < self.ncol:
                if self.board[index] == player:
                    num += 1
                else:
                    num = 0

                if num >= 4:
                    return True

                index = (index[0] + 1, index[1] + 1)
            if i == 0 and j < self.nrow - 4:
                j += 1
            else:
                j = 0
                i += 1

        return False
