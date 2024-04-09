from collections import namedtuple
players = {0: 'X', 1: 'O'} # X is Player, O is CPU
def help(g):
    print("Supported Commands: ")
    for cmd in cmds:
        print(cmd, cmds[cmd])
def undo(g):
    g.undo() # place in
def reset(g):
    g.reset() #place in 
cmds = {'h': help, 'u': undo, 'r': reset} # commands
def reward(act):
    return 0
def output(T, act, ract=None):
    mess = "Player " + str(players[T]) + " Selected Box #" + str(act)
    if(ract):
        print(mess + ", However a random box (Box #" + str(ract) + ")  instead selected. Probability  happening during any move is: " + str(T))
    else:
        print(mess)