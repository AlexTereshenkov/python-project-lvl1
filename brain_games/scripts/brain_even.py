#!/usr/bin/env python

from brain_games.games.even_or_odd import get_even_or_odd_data
from brain_games.play import play_flow


def main():
    play_flow(game_data_getter=get_even_or_odd_data)


if __name__ == "__main__":
    main()
