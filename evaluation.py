import chess
from collections import Counter
from typing import List, Tuple, Dict
from config import (piece_type_to_value_mg, piece_type_to_value_eg, PAWN_WEAKNESS_FACTOR, MATE_EVAL, 
                    GAME_PHASE_MIN_EG, GAME_PHASE_MAX_MG, GAME_PHASE_RANGE)
from pst import PstFactory, GamePhase
from enum import Enum

# ideas
# piece value tables for opening and endgame: https://www.chessprogramming.org/Tapered_Eval
# tapered evaluation: https://www.chessprogramming.org/Tapered_Eval



def evaluate(board: chess.Board) -> float:
    """
    Implementation of a basic tapered evaluation function.

    It takes into account:
    - material values for middlegame and endgame, weighted by game phase
    - piece square tables for middlegame and endgame, weighted by game phase
    - correction factors for pawn weaknesses

    Parameters:
        board (chess.Board): chess.Board object containing current state of the board

    Returns:
        float: the approximate centipawn evaluation of the position (+100 ~ 1 pawn in favour of white)
    """
    # determine the game phase and weights to apply for tapered evaluation
    game_phase = calculate_game_phase(board)
    factor_mg = (game_phase - GAME_PHASE_MIN_EG) / GAME_PHASE_RANGE
    factor_eg = 1 - factor_mg

    eval = 0
    # Sum the piece values
    for square in chess.SQUARES:
        if piece := board.piece_at(square):
            piece_type, color = piece.piece_type, piece.color
            material_mg = piece_type_to_value_mg[piece_type]
            pst_mg = PstFactory.get_pst(piece_type, color, GamePhase.MIDDLEGAME)[square]
            material_eg = piece_type_to_value_eg[piece_type]
            pst_eg = PstFactory.get_pst(piece_type, color, GamePhase.ENDGAME)[square]
            value = factor_mg * (material_mg + pst_mg) + factor_eg * (material_eg + pst_eg)
            eval += value if piece.color == chess.WHITE else -value

    # Factor in isolated and doubled pawns
    white_pawns = board.pieces(chess.PAWN, chess.WHITE)
    black_pawns = board.pieces(chess.PAWN, chess.BLACK)
    eval -= PAWN_WEAKNESS_FACTOR * (
        count_isolated_pawns(white_pawns) - count_isolated_pawns(black_pawns)
    )
    eval -= PAWN_WEAKNESS_FACTOR * (
        count_doubled_pawns(white_pawns) - count_doubled_pawns(black_pawns)
    )

    return eval


def calculate_game_phase(board: chess.Board) -> float:
    """
    Calculates a float which represents the 'game phase' of the current position.
    The lower the game phase, the closer we are to the endgame.

    Parameters:
        board (chess.Board): chess.Board object containing current state of the board

    Returns:
        float: value of game phase bounded by GAME_PHASE_MAX_MG, and GAME_PHASE_MIN_EG
    """
    # The game phase is defined as the sum of the middlegame values of all the pieces except pawns.
    game_phase = 0
    for square in chess.SQUARES:
        if piece := board.piece_at(square):
            game_phase += piece_type_to_value_mg[piece.piece_type]
    game_phase = max(GAME_PHASE_MIN_EG, min(GAME_PHASE_MAX_MG, game_phase))
    return game_phase


def count_isolated_pawns(pawn_squares: chess.SquareSet) -> int:
    """
    Count the number of isolated pawns.
    """
    files = [chess.square_file(square) for square in pawn_squares]
    file_set = set(files)
    count = 0
    for f in files:
        if (f - 1) not in file_set and (f + 1) not in file_set:
            count += 1
    return count


def count_doubled_pawns(pawn_squares: chess.SquareSet) -> int:
    """
    Count the number of doubled pawns. Tripled pawns are counted twice.
    """
    files = Counter([chess.square_file(square) for square in pawn_squares])
    count = 0
    for f in files:
        pawns_on_file = files.get(f, 0)
        if pawns_on_file == 2:
            count += 1
        elif pawns_on_file > 2:
            count += 2
    return count
