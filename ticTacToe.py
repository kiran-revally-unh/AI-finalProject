import pickle
import numpy as np

BRD_RWS = 3
BRD_CLS = 3


class State:
    def __init__(self, p1, p2):
        self.board = np.zeros((BRD_RWS, BRD_CLS))
        #For Player 1
        self.p1 = p1

         # getting hash of board state which is unique
    def getHash(self):
        self.boardHash = str(self.board.reshape(BRD_CLS * BRD_RWS))
        return self.boardHash