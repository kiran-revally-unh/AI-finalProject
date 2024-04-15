from tictactoe import TicTacToe
from agents import *
from util import *

AGENT = ExpectimaxAgent

def run(gameplay, agents_1):
    if(gameplay.gstate.T == 1):

        print("It is CPU's Turn: ")
        action = agents_1.getMove(gameplay.gstate, 0.95, 0.0, 4)
        gameplay.gstate = gameplay.transition(act)
        return

    print("It is Your Turn: ")
    cmd = getInput(gameplay)
    handleInput(gameplay, cmd)