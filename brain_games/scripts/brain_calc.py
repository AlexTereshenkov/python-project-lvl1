#!/usr/bin/env python

from brain_games.games.calculator import get_calculator_data
from brain_games.play import play_flow


def main():
    play_flow(game_data_getter=get_calculator_data)


if __name__ == "__main__":
    main()
