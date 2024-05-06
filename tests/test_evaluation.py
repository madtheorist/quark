import pytest
import chess
from evaluation import (evaluate_shannon,
                        count_isolated_pawns, 
                        count_doubled_pawns)

class TestEvaluation:

    def test_evaluate_shannon(self, starting_position):
        # starting position
        assert evaluate_shannon(starting_position) == 0
        # white up on material
        white_up = chess.Board('r1bqkb1r/ppp2ppp/2p2n2/8/4P3/8/PPPP1PPP/RNBQKB1R w KQkq - 0 1')
        assert evaluate_shannon(white_up) > 0
        # black up on material
        black_up = chess.Board('2r1q3/1k6/8/8/8/8/3K4/3R4 w - - 0 1')
        assert evaluate_shannon(black_up) < 0
        # equal material, white has better pawn structure
        white_up = chess.Board('2kr4/3p1p2/3p1p2/1P1P4/P1P5/2K5/8/4R3 w - - 0 1')
        assert evaluate_shannon(white_up) > 0

    def test_count_isolated_pawns(self, starting_position):
        square_set = starting_position.pieces(chess.PAWN, chess.WHITE)
        assert count_isolated_pawns(square_set) == 0
        square_set = ([chess.A2, chess.C3, chess.C4])
        assert count_isolated_pawns(square_set) == 3

    def test_count_doubled_pawns(self, starting_position):
        square_set = starting_position.pieces(chess.PAWN, chess.WHITE)
        assert count_doubled_pawns(square_set) == 0
        square_set = ([chess.A2, chess.C3, chess.C4])
        assert count_doubled_pawns(square_set) == 1
