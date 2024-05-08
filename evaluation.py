import chess
from collections import Counter
from config import piece_type_to_value, PAWN_WEAKNESS_FACTOR, MATE_EVAL

# ideas
# piece value tables for opening and endgame: https://www.chessprogramming.org/Tapered_Eval
# tapered evaluation: https://www.chessprogramming.org/Tapered_Eval


def evaluate(board: chess.Board) -> float:
    """
    Implementation of Shannon's crude evaluation function as outlined in this 1949 paper
    https://www.pi.infn.it/%7Ecarosi/chess/shannon.txt
    combined with piece square tables and corrections for pawn weaknesses, etc.

    Parameters:
        board (chess.Board): chess.Board object containing current state of the board

    Returns:
        float: the approximate centipawn evaluation of the position (+100 ~ 1 pawn in favour of white)
    """
    eval = 0
    # Sum the piece values
    for square in chess.SQUARES:
        if piece := board.piece_at(square):
            value = piece_type_to_value[piece.piece_type]
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
