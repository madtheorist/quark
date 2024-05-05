import pytest
import chess
from evaluation import (evaluate_shannon,
                        count_isolated_pawns, 
                        count_doubled_pawns)

def test_evaluate_shannon(starting_position):
    assert evaluate_shannon(starting_position) == 0

def test_count_isolated_pawns(starting_position):
    square_set = starting_position.pieces(chess.PAWN, chess.WHITE)
    assert count_isolated_pawns(square_set) == 0
    square_set = ([chess.A2, chess.C3, chess.C4])
    assert count_isolated_pawns(square_set) == 3

def test_count_doubled_pawns(starting_position):
    square_set = starting_position.pieces(chess.PAWN, chess.WHITE)
    assert count_doubled_pawns(square_set) == 0
    square_set = ([chess.A2, chess.C3, chess.C4])
    assert count_doubled_pawns(square_set) == 1
