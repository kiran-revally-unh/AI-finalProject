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

    
    #Taking action and gameState update

    def transition(self, act):
        acts,board,t  = self.gstate
        Random_Action1 = None 
        newt, newBoard, newActions = (T+1)%2, copy.deepcopy(board), list(actions)  
        #Selecting Random Action      
        if(np.random.random() < P): 
            #Condition for Random Action     
            Random_Action1 = np.random.choice([i for i in range(len(acts)) if acts[i]])
        #Displaying action of the player
        output(T, act, Random_Action1)
        if(Random_Action1):
            act = Random_Action1
        r, c = dcdAction(act, self.n)
        newBoard[r][c] = t
        newActions[act] = 0
        newState = GameState(newt, newBoard, newActions)
        self.states.append(newState)
        return newState