# algorithms explained - minimax and alpha-beta pruning
# https://www.youtube.com/watch?v=l-hh51ncgDI

def minimax(position, depth, alpha, beta, player):
    if depth == 0 or game_over(position):
        return position
    if player == maxPlayer:
        maxEval = -inf
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, minPlayer)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:  # alpha is already bigger than parent's beta
                break          # max node can only get bigger
        return maxEval
    else:
        minEval = +inf
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, maxPlayer)
            mixEval = min(maxEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:  # beta is already bigger than parent
                break          # min node can only get smaller
        return minEval
