#!/usr/bin/env python

from brain_games.games.calculator import play_calculator
from brain_games.configs import TRIALS_COUNT


def main():
    play_calculator(trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
