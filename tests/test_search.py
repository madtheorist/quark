import pytest
import chess
from search import next_move


class TestSearch:

    depth = 3

    def test_knight_fork_white(self):
        board = chess.Board("3q3k/8/8/6N1/8/6P1/8/5K2 w - - 0 1")
        assert next_move(board, self.depth) == chess.Move.from_uci("g5f7")

    def test_knight_fork_black(self):
        board = chess.Board("3kr3/8/8/5n2/8/8/2R3K1/8 b - - 0 1")
        assert next_move(board, self.depth) == chess.Move.from_uci("f5e3")

    def test_mate_in_two_white(self):
        board = chess.Board("2Q4r/4prk1/ppp2p1p/8/2qP1R2/2P5/P5PP/5RK1 w - - 4 33")
        assert next_move(board, self.depth) == chess.Move.from_uci("f4g4")