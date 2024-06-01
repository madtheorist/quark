![Unit tests](https://github.com/madtheorist/patzer-bot/actions/workflows/python-app.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Quark

This is a small side project to build a chess engine in Python, leveraging the excellent [python-chess](https://github.com/niklasf/python-chess) library by Niklas Fiekas. It is very much still a work in progress; I am a complete beginner to chess programming.

Quark currently implements:
- the [minimax search algorithm](https://en.wikipedia.org/wiki/Minimax) with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning);
- a tapered evaluation function. 'Tapered' means that **two** sets of piece values and piece square tables are used, one set for the middlegame and the other set for the endgame, with the weight of each determined by linear interpolation.
    - the piece square tables were obtained from those used by [rofChade](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19);
- evaluation corrections for pawn weaknesses, including isolated and doubled pawns;
- a game UI that allows you to play against the bot in the terminal window.

I drew inspiration from the following sources:
- [Andoma](https://github.com/healeycodes/andoma/tree/main) by Andrew Healey. This was a simple and accessible introduction to chess programming.
- [Blunder](https://github.com/deanmchris/blunder). I don't know Golang, but it's surprisingly readable coming from a Python background.
- The [Chess Programming Wiki](https://www.chessprogramming.org/Main_Page). A treasure trove of information about chess programming. You can go down a lot of rabbit holes if you aren't careful.

## Installation

Create a virtual environment and install dependencies (commands may vary depending on OS).

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run tests with pytest, run

```
pytest
```

in the root directory. More complete tests to come; development is still ongoing.

## Play against the bot in the terminal

Once installed, you can play against Quark at the default depth (set in config.py) in the terminal by running

```
python game.py
```

## Play against the bot on Lichess

When Quark is in a more mature state I'll eventually hook it up to Lichess.