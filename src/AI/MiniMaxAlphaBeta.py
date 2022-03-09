import copy
import sys

def Minimax(game, depth, isMax, alpha, beta):
    temp = copy.deepcopy(game)
    if depth == 0 | TerminalState(temp):
        return Evaluation(temp)
    if (isMax):
        maxEvaluation = sys.maxint
        for i in range(6):
            isValidMove = temp.take_slot(i)
            if (isValidMove):
                eval = Minimax(temp,depth - 1,False, alpha, beta)
                maxEvaluation = max(maxEvaluation,eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEvaluation
    else:
        minEvaluation = sys.minint
        for i in range(6):
            isValidMove = temp.take_slot(i)
            if (isValidMove):
                eval = Minimax(temp, depth - 1, True, alpha, beta)
                minEvaluation = min(minEvaluation, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
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
