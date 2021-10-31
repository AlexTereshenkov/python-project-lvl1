#!/usr/bin/env python

from brain_games.games.gcd import play_gcd
from brain_games.configs import TRIALS_COUNT


def main():
    play_gcd(trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
