import sys
import chess
from typing import List
from search import next_move
from config import DEFAULT_DEPTH

def main():

    board = chess.Board()

    while True:
        command = input()
        command = command.strip()

        if command == 'uci':
            uci()

        elif command == 'debug':
            pass

        elif command == 'isready':
            print('readyok')
        
        elif command == 'quit':
            sys.exit()

        elif command == 'ucinewgame':
            pass

        elif command.startswith("position"):
            position(command, board)

        elif command.startswith("go"):
            go(board)

def uci():
    """
    Respond to the uci command "uci"
    """
    print("id name Quark")
    print("id author Jesse Wang")
    print("uciok")

def position(command: str, board: chess.Board):
    """
    Response to the uci command "position":

    position [fen <fenstring> | startpos ]  moves <move1> .... <movei>
	set up the position described in fenstring on the internal board and
	play the moves on the internal chess board.
    """
    words: List[str] = command.split(" ")

    if len(words) < 2:
        return

    if words[1] == "startpos":
        board.reset()
        if len(words) > 2 and words[2] == "moves":
            moves = words[3:]
            for move in moves:
                board.push_uci(move)
        
    elif words[1] == "fen":
        fen = " ".join(words[2:8])
        board.set_fen(fen)
        if len(words) > 8 and words[8] == "moves":
            moves = words[9:]
            for move in moves:
                board.push_uci(move)

def go(board: chess.Board):
    """
    Respond to the uci command "go"
    Given the board, return the best move
    """
    best_move = next_move(board, DEFAULT_DEPTH)
    print(f"bestmove {best_move}")

if __name__ == "__main__":
    main()