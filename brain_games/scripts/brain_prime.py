#!/usr/bin/env python

from brain_games.games.prime import play_prime
from brain_games.configs import TRIALS_COUNT


def main():
    play_prime(trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
