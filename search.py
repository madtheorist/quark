import chess
import time
from evaluation import evaluate
from typing import List, Literal
from config import piece_type_to_value_mg, MATE_EVAL



def next_move(board: chess.Board, depth: int, debug=True) -> chess.Move:
    """
    Parameters:
        board (chess.Board): chess.Board object representing current state of board
        depth (int): tree depth of negamax search algorithm

    Returns:
        chess.Move: optimal move found
    """
    t0 = time.time()
    if board.turn == chess.WHITE:
        move = negamax_root(board, depth, -float("inf"), float("inf"), 1)
    else:
        move = negamax_root(board, depth, -float("inf"), float("inf"), -1)
    if debug:
        print(f"elapsed time: {(time.time() - t0):.2f} seconds")
    return move


def negamax_root(
    board: chess.Board,
    depth: int,
    alpha: float,
    beta: float,
    color: Literal[1, -1],
) -> chess.Move:
    """
    Root function for negamax algorithm
    """
    optimal_value = -float("inf")
    for move in sort_moves(board):
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


def negamax(
    board: chess.Board,
    depth: int,
    alpha: float,
    beta: float,
    color: Literal[1, -1],
) -> float:
    """
    Implementation of negamax algorithm with alpha-beta pruning
    https://en.wikipedia.org/wiki/Negamax

    Returns
        float: evaluation of position
    """
    if outcome := board.outcome():
        if outcome.termination == chess.Termination.CHECKMATE:
            if outcome.winner == chess.WHITE:
                return color * MATE_EVAL
            else:
                return -color * MATE_EVAL
        else:
            return 0
    
    if depth == 0:
        return color * evaluate(board)

    value = -float("inf")
    for move in sort_moves(board):
        board.push(move)
        value = max(value, -negamax(board, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)
        board.pop()
        if alpha >= beta:
            break
    return value


def sort_moves(board: chess.Board) -> List[chess.Move]:
    """
    Sort all the legal moves given the current board. 
    Captures > non-captures.
    To sort the captures, we use the Most Valuable Victim - Least Valuable Aggressor (MVV-LVA) heuristic.
    """
    captures, non_captures = [], []

    for move in board.legal_moves:
        if board.is_capture(move):
            captures.append(move)
        else:
            non_captures.append(move)

    if captures:
        captures = sorted(captures, key=lambda x: mvv_lva(board, x), reverse=True)

    return captures + non_captures


def mvv_lva(board: chess.Board, move: chess.Move) -> int:
    """
    calculate the value of a capture using MVV-LVA
    the higher the value, the better
    """
    if board.is_en_passant(move):
        return 0
    aggressor = board.piece_at(move.from_square)
    victim = board.piece_at(move.to_square)
    val = piece_type_to_value_mg[victim.piece_type] - piece_type_to_value_mg[aggressor.piece_type]
    return val