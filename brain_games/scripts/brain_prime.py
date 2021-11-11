#!/usr/bin/env python

from brain_games.games.prime import get_prime_data
from brain_games.play import play_flow


def main():
    play_flow(game_data_getter=get_prime_data)


if __name__ == "__main__":
    main()
