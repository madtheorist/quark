import chess
from chess import InvalidMoveError, IllegalMoveError, AmbiguousMoveError
from config import fen_to_icon, DEPTH
from search import next_move
from dataclasses import dataclass

"""
A simple game interface to play against the bot.
"""


@dataclass
class Player:
    """
    Simple dataclass representing a player
    """

    name: str
    is_bot: bool
    wins: int = 0
    draws: int = 0
    losses: int = 0

    @property
    def record(self):
        return f"{self.wins}-{self.draws}-{self.losses} (W-D-L)"


class Game:
    """
    Object representing a chess game
    """

    def __init__(self, board: chess.Board, white_player: Player, black_player: Player):
        self.board = board
        self.white_player = white_player
        self.black_player = black_player

    def display_board(self) -> None:
        """
        Prints visual representation of the board to the terminal.
        Displays correct orientation of the board depending on which
        """
        # get FEN representation of board with slashes replaced by \n characters
        display = list(str(self.board))
        for i, char in enumerate(display):
            if icon := fen_to_icon.get(char):
                display[i] = icon
        if self.board.turn == chess.BLACK:
            display.reverse()
        display_str = "".join(display)
        print(display_str)

    def play(self) -> None:
        """
        Main loop to play the game.
        """
        while not board.is_game_over():
            if self.board.turn == chess.WHITE:
                player = self.white_player
            else:
                player = self.black_player

            if player.is_bot:
                move = next_move(self.board, DEPTH, debug=False)
                board.push(move)
            else:
                self.display_board()
                san = input(
                    "Enter a valid chess move in standard algebraic notation, like d4, Nxe4, or e8=Q:\n"
                )
                try:
                    self.board.push_san(san)
                except InvalidMoveError:
                    print("Notation is not recognised. Please try again.")
                except IllegalMoveError:
                    print("Illegal move. Please try again.")
                except AmbiguousMoveError:
                    print("Move is ambiguous. Please be more specific.")

        print(f"\nResult: [w] {board.result()} [b]")


if __name__ == "__main__":

    board = chess.Board()
    user, bot = Player("User", False), Player("Quark", True)

    try:
        print("Welcome to the quark bot UI. Press control-C to exit.")
        user_color = input("Would you like to play as [w]hite or [b]lack?\n")
        from_pos = input("Would you like to play from an existing position? [y/n]\n")
        if from_pos.lower() == 'y':
            fen = input("Please paste the FEN of the position you would like to play from: \n")
            try:
                board = chess.Board(fen)
            except ValueError:
                print("Invalid FEN. Using starting position instead.")

        if user_color.lower() == "w":
            game = Game(board, user, bot)
        else:
            game = Game(board, bot, user)

        game.play()

    except KeyboardInterrupt:
        print("Thanks for playing!\n")
