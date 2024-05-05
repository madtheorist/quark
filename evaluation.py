import chess
from collections import Counter

piece_type_to_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

PAWN_WEAKNESS_FACTOR = 50

def evaluate_shannon(board: chess.Board) -> float:
    """
    Implementation of Shannon's crude evaluation function as outlined in this 1949 paper
    https://www.pi.infn.it/%7Ecarosi/chess/shannon.txt
    
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
    eval -= PAWN_WEAKNESS_FACTOR * (count_isolated_pawns(white_pawns) - count_isolated_pawns(black_pawns))
    eval -= PAWN_WEAKNESS_FACTOR * (count_doubled_pawns(white_pawns) - count_doubled_pawns(black_pawns))

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
        if files.get(f) == 2:
            count += 1
        elif files.get(f) > 2:
            count += 2
    return count
    