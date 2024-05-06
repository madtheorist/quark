import chess
import time
from evaluation import evaluate


def next_move(board: chess.Board, depth: int, debug=True) -> chess.Move:
    """
    Parameters:
        board (chess.Board): chess.Board object representing current state of board
        depth (int): tree depth of negamax search algorithm

    Returns:
        chess.Move: optimal move found
    """
    t0 = time.time()
    color = 1 if board.turn == chess.WHITE else -1
    move = negamax_root(board, depth, -float("inf"), float("inf"), color)
    if debug:
        print(f"elapsed time: {(time.time() - t0):.2f} seconds")
    return move

def negamax_root(board: chess.Board, 
                 depth: int,
                 alpha: float,
                 beta: float,
                 color: bool,
) -> chess.Move:
    """
    Root function for negamax algorithm
    """
    optimal_value = -float("inf")
    legal_moves = board.legal_moves
    for move in legal_moves:
        board.push(move)
        value = -negamax(board, depth - 1, -beta, -alpha, -color)
        board.pop()
        if value > optimal_value:
            optimal_value = value
            best_move = move
        alpha = max(optimal_value, alpha)
        if alpha > beta:
            break
    return best_move
        

def negamax(board: chess.Board, 
            depth: int, 
            alpha: float, 
            beta: float, 
            color: bool,
) -> float:
    """
    Implementation of negamax algorithm with alpha-beta pruning
    https://en.wikipedia.org/wiki/Negamax

    Returns
        float: absolute value of evaluation of position (>=0)
    """
    if depth == 0:
        return color * evaluate(board)
    
    value = -float("inf")
    for move in board.legal_moves:
        board.push(move)
        value = max(value, -negamax(board, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)
        board.pop()
        if alpha >= beta:
            return value

    return value

