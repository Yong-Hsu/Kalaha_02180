import copy
import sys

def Minimax(game, depth, isMax):
    temp = copy.deepcopy(game)
    if depth == 0 | TerminalState(temp):
        return Evaluation(temp)
    if (isMax):
        maxEvaluation = sys.maxint
        for i in range(6):
            temp.take_slot(i)
            eval = Minimax(temp,depth - 1,False)
            maxEvaluation = max(maxEvaluation,eval)
        return maxEvaluation
    else:
        minEvaluation = sys.minint
        for i in range(6):
            temp.take_slot(i)
            eval = Minimax(temp, depth - 1, True)
            minEvaluation = min(minEvaluation, eval)
        return minEvaluation

def TerminalState(game):
    game.is_terminal_state()


#Rank on number of peices the action/move yields
def Evaluation(game):
    if (TerminalState(game)):
        return 4
    elif ("Repeating move")
        return
    elif ("opposite move")
        return
    else
        return
