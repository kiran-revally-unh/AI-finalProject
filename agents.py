import os
import collections
import numpy as np
import random
import numpy as np
import pandas as pd
from util import *

values = {}
qvalues = {}
# overview  of system agent

class Agent():
    def __init__(self, A):
        self.A = A
    def check(self, gstate): #Cheking possible AxA for all sub-grids of gameStates
        Boards = np.matrix(gstate.Boards)
        l = len(Boards)
        A = self.A
        for i in range(l-A+1):
            for j in range(l-A+1):
                won, winner = self.checkBox(Boards[i:i+A,j:j+A].tolist())
                if(won):
                    return True, winner
        return False, None
    def checkBox(self, Boards): #Exploring 1 sub-grid
        l = len(Boards)
        for i in range(l): # Horizontal examine
            if(Boards[i][0] >= 0 and all(Boards[i][j] == Boards[i][j+1] for j in range(l-1))):
                return True, Boards[i][0]
        for j in range(l): # vertical examine
            if(Boards[0][j] >= 0 and all([Boards[i-1][j] == Boards[i][j] for i in range(1, l)])):
                return True, Boards[0][j]
        if Boards[0][0] >= 0 and all([Boards[i-1][i-1] == Boards[i][i] for i in range(1, l)]):#1st diagonal examine
            return True, Boards[0][0]
        if Boards[0][-1] >= 0 and all([Boards[i-1][l-i] == Boards[i][l-i-1] for i in range(1, l)]): #2nd diagonal examine
            return True, Boards[0][-1]
        return False, None
    def score(self, gstate, Le, p, d, w, de):
        if(str(gstate) in values):
            return values[str(gstate)]
        won, winner = self.check(gstate)
        if(won):
            values[str(gstate)] = w if(winner==0) else -w #Win Score to be shown
            return values[str(gstate)]
        actions = gstate.actions
        if(sum(actions)==0 or de==D):
            values[str(gstate)] = 0
            return 0
        return(self.computeScore_1(gstate, Le, p, d, w, de))
    def qScore(self, gstate, action, Le, p, d, w):
        qstate = str(gstate) + str(action)
        if qstate in qvalues:
            return qvalues[qstate]
        sc = reward(action)
        for s, p in self.transition(gstate, action, p):
            sc += Le * p * self.score(s, Le, p, d, w, 0)
        qvalues[qstate] = sc
        return sc
    def update(self, gstate, action):
        newT = (gstate.T+1)%2
        newBoards = copy.deepcopy(gstate.Boards)
        l = len(newBoards)
        r,c = dcdAction(action, l)
        newBoards[r][c] = gameState.T
        newActions = list(gameState.actions)
        newActions[action] = 0
        newState = GameState(newT, newBoards, newActions)
        return newState
    def getMove(self, gstate, Le=1, p=0, d=5, w=1000):
        minQ, optimalAction = float('inf'), None
        ties = []
        actions = gstate.actions
        for i, action in enumerate(actions):
            if(action):
                q = self.qScore(gstate, i, Le, p, d, w)
                if(q < minQ):
                    minQ, optimalAction = q, i
                    ties = []
                elif(q == minQ):
                    ties.append(i)
        if(ties):
            return np.random.choice(ties)
        return optimalAction
    def transition(self, gstate, action, P):
        newState = self.update(gameState, action)
        yield(newState, float(1-P))
        if(P > 0): #P is the chance of a random move being forced
            for randAction, possible in enumerate(actions):
                if(possible):
                    newState = self.update(gameState, randAction)
                    yield(newState, (float(P)/sum(actions))) #Random game state probabilities_
    def printVals(self, gstate):
        V = {}
        for i, action in enumerate(gstate.actions):
            if(action):
                for newState, _ in self.transition(gstate, i):
                    V[str(newState)] = L * self.score(newState)
        print(V)
        return V