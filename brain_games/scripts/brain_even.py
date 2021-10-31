#!/usr/bin/env python

from brain_games.games.even_or_odd import play_even_or_odd
from brain_games.configs import TRIALS_COUNT


def main():
    play_even_or_odd(trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
