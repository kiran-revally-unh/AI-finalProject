from tictactoe import TicTacToe
from agents import *
from util import *

AGENT = ExpectimaxAgent

def run(gameplay, agents_1):
  

    print("It is Your Turn: ")
    cmd = getInput(gameplay)
    handleInput(gameplay, cmd)