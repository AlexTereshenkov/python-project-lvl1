#!/usr/bin/env python

from brain_games.games.gcd import get_gcd_data
from brain_games.play import play_flow


def main():
    play_flow(game_data_getter=get_gcd_data)


if __name__ == "__main__":
    main()
