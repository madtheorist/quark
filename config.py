import chess

# Material value
piece_type_to_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# Correction factor for pawn weaknesses 
PAWN_WEAKNESS_FACTOR = 50
MATE_EVAL = 1_000_000_000

# Piece square tables - a kind of 'second order correction' to material value depending on
# where the piece is located, and the game stage
# source: Rofchade - https://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19