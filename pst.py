import chess
from typing import List, Tuple, Dict
from enum import Enum
from config import *


class GamePhase(Enum):
    MIDDLEGAME = "middlegame"
    ENDGAME = "endgame"


class PstFactory:
    """
    Factory pattern to register and get piece square tables depending on piece type, color, and game phase
    """

    piece_square_tables: Dict[Tuple, List[int]] = {}

    @classmethod
    def get_pst(
        cls, piece_type: chess.PieceType, color: chess.Color, phase: GamePhase
    ) -> List[int]:
        if pst := cls.piece_square_tables.get((piece_type, color, phase)):
            return pst
        raise ValueError(
            f"Piece square table not yet registered for {piece_type}, {color}, {phase} combination"
        )

    @classmethod
    def register_pst(
        cls,
        pst: List[int],
        piece_type: chess.PieceType,
        color: chess.Color,
        phase: GamePhase,
    ):
        key = (piece_type, color, phase)
        if key in cls.piece_square_tables:
            raise ValueError(f"Piece square table for {key} already registered")
        cls.piece_square_tables[(piece_type, color, phase)] = pst


PstFactory.register_pst(white_pawn_mg, chess.PAWN, chess.WHITE, GamePhase.MIDDLEGAME)
PstFactory.register_pst(
    white_knight_mg, chess.KNIGHT, chess.WHITE, GamePhase.MIDDLEGAME
)
PstFactory.register_pst(
    white_bishop_mg, chess.BISHOP, chess.WHITE, GamePhase.MIDDLEGAME
)
PstFactory.register_pst(white_rook_mg, chess.ROOK, chess.WHITE, GamePhase.MIDDLEGAME)
PstFactory.register_pst(white_queen_mg, chess.QUEEN, chess.WHITE, GamePhase.MIDDLEGAME)
PstFactory.register_pst(white_king_mg, chess.KING, chess.WHITE, GamePhase.MIDDLEGAME)

PstFactory.register_pst(black_pawn_mg, chess.PAWN, chess.BLACK, GamePhase.MIDDLEGAME)
PstFactory.register_pst(
    black_knight_mg, chess.KNIGHT, chess.BLACK, GamePhase.MIDDLEGAME
)
PstFactory.register_pst(
    black_bishop_mg, chess.BISHOP, chess.BLACK, GamePhase.MIDDLEGAME
)
PstFactory.register_pst(black_rook_mg, chess.ROOK, chess.BLACK, GamePhase.MIDDLEGAME)
PstFactory.register_pst(black_queen_mg, chess.QUEEN, chess.BLACK, GamePhase.MIDDLEGAME)
PstFactory.register_pst(black_king_mg, chess.KING, chess.BLACK, GamePhase.MIDDLEGAME)

PstFactory.register_pst(white_pawn_eg, chess.PAWN, chess.WHITE, GamePhase.ENDGAME)
PstFactory.register_pst(white_knight_eg, chess.KNIGHT, chess.WHITE, GamePhase.ENDGAME)
PstFactory.register_pst(white_bishop_eg, chess.BISHOP, chess.WHITE, GamePhase.ENDGAME)
PstFactory.register_pst(white_rook_eg, chess.ROOK, chess.WHITE, GamePhase.ENDGAME)
PstFactory.register_pst(white_queen_eg, chess.QUEEN, chess.WHITE, GamePhase.ENDGAME)
PstFactory.register_pst(white_king_eg, chess.KING, chess.WHITE, GamePhase.ENDGAME)

PstFactory.register_pst(black_pawn_eg, chess.PAWN, chess.BLACK, GamePhase.ENDGAME)
PstFactory.register_pst(black_knight_eg, chess.KNIGHT, chess.BLACK, GamePhase.ENDGAME)
PstFactory.register_pst(black_bishop_eg, chess.BISHOP, chess.BLACK, GamePhase.ENDGAME)
PstFactory.register_pst(black_rook_eg, chess.ROOK, chess.BLACK, GamePhase.ENDGAME)
PstFactory.register_pst(black_queen_eg, chess.QUEEN, chess.BLACK, GamePhase.ENDGAME)
PstFactory.register_pst(black_king_eg, chess.KING, chess.BLACK, GamePhase.ENDGAME)
