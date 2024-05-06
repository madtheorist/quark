import chess
import pytest


@pytest.fixture()
def starting_position():
    return chess.Board()
