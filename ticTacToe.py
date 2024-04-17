import pickle
import numpy as np

BRD_RWS = 3
BRD_CLS = 3


class State:
    def __init__(self, p1, p2):
        self.board = np.zeros((BRD_RWS, BRD_CLS))
        #For Player 1
        self.p1 = p1
        #For Player 2
        self.p2 = p2
        self.isEnd = False
        #Giving Conditions
        self.boardHash = None
        # Player 1's turn
        self.playerSymbol = 1

    # getting hash of board state which is unique
    def getHash(self):
        self.boardHash = str(self.board.reshape(BRD_CLS * BRD_RWS))
        return self.boardHash

    def winner(self):
        # Defining rows
        for i in range(BRD_RWS):
            if sum(self.board[i, :]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[i, :]) == -3:
                self.isEnd = True
                return -1
        # Defining Columns
        for i in range(BRD_CLS):
            if sum(self.board[:, i]) == 3:
                self.isEnd = True
                return 1
            if sum(self.board[:, i]) == -3:
                self.isEnd = True
                return -1
        # Defining Diagonal
        diag_sum1 = sum([self.board[i, i] for i in range(BRD_CLS)])
        diag_sum2 = sum([self.board[i, BRD_CLS - i - 1] for i in range(BRD_CLS)])
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if diag_sum == 3:
            self.isEnd = True
            if diag_sum1 == 3 or diag_sum2 == 3:
                return 1
            else:
                return -1

        # If there are no positions available
        if len(self.availablePositions()) == 0:
            self.isEnd = True
            return 0
        # not the end
        self.isEnd = False
        return None
    
    def availablePositions(self):
        positions = []
        for i in range(BRD_RWS):
            for j in range(BRD_CLS):
                if self.board[i, j] == 0:
                    positions.append((i, j))  # need to be tuple
        return positions