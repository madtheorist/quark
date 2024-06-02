import pytest
import chess
from search import next_move
from config import DEFAULT_DEPTH


class TestSearch:

    def test_knight_fork_white(self):
        board = chess.Board("3q3k/8/8/6N1/8/6P1/8/5K2 w - - 0 1")
        assert next_move(board, DEFAULT_DEPTH) == chess.Move.from_uci("g5f7")

    def test_knight_fork_black(self):
        board = chess.Board("3kr3/8/8/5n2/8/8/2R3K1/8 b - - 0 1")
        assert next_move(board, DEFAULT_DEPTH) == chess.Move.from_uci("f5e3")

    def test_mate_in_two_white(self):
        board = chess.Board("2Q4r/4prk1/ppp2p1p/8/2qP1R2/2P5/P5PP/5RK1 w - - 4 33")
        assert next_move(board, DEFAULT_DEPTH) == chess.Move.from_uci("f4g4")

    def test_mate_in_one_black(self):
        board = chess.Board("rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 2")
        assert next_move(board, DEFAULT_DEPTH) == chess.Move.from_uci("d8h4")