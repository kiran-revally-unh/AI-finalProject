import copy
import numpy as np
from util import *
from enum import Enum
from agents import Agent

MODE = "three"

n     = 3                 # Defining a N X N grid  for the game
p = 0.0             # P which is Random
w     = 100              # Reward for Win
t     = 0                 # Zero is definied for a Player, One is definied for computer
d     = 3                 # Maximum Search into Depth
l     = 0.95              # Decaying factor
k     = 3                 # Nummer of squares in a row whivh is needed to win
qvalues = {}                # Stored Values
valuess  = {}                # State Values


class TicTacToe():
    def __init__(self, n=n, k=k):
        self.gameState = getGameState(n)
        self.states = [self.gstate]
        self.n = n
        self.k = k