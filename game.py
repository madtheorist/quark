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
    def record(self) -> str:
        return f"{self.wins}-{self.draws}-{self.losses} (W-D-L)"

    @property
    def score(self) -> str:
        return f"{self.wins + 0.5 * self.draws:.1f}"


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
                san = board.san(move)
                board.push(move)
                print(f"Quark played the move {san}.")
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

        self._update_player_records()
        print(f"\nResult: [w] {board.result()} [b]\n")
        print(
            f"""The current scores of the players are:\n{self.white_player.name} {self.white_player.score}-{self.black_player.score} {self.black_player.name}
              """
        )

    def _update_player_records(self) -> None:
        """
        Update number of wins, losses, and draws of players.
        """
        outcome = self.board.outcome()
        if outcome.winner == chess.WHITE:
            self.white_player.wins += 1
            self.black_player.losses += 1
        elif outcome.winner == chess.BLACK:
            self.white_player.losses += 1
            self.black_player.wins += 1
        else:
            self.white_player.draws += 1
            self.black_player.draws += 1


if __name__ == "__main__":

    user, bot = Player("User", False), Player("Quark", True)
    in_play = True

    while in_play:
        try:
            print("Welcome to the quark bot UI. Press control-C to exit.")
            user_color = input("Would you like to play as [w]hite or [b]lack?\n")
            from_pos = input("Would you like to play from an existing position? [y/n]\n")
            board = chess.Board()
            if from_pos.lower() == "y":
                fen = input(
                    "Please paste the FEN of the position you would like to play from: \n"
                )
                try:
                    board = chess.Board(fen)
                except ValueError:
                    print("Invalid FEN. Using starting position instead.")

            if user_color.lower() == "w":
                game = Game(board, user, bot)
            else:
                game = Game(board, bot, user)

            game.play()

            again = input("Play again? [y/n]\n")
            if again.lower() != "y":
                in_play = False

        except KeyboardInterrupt:
            in_play = False
    
    print('Thanks for playing!')