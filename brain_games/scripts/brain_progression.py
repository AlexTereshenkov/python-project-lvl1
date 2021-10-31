#!/usr/bin/env python

from brain_games.games.progression import play_progression
from brain_games.configs import TRIALS_COUNT


def main():
    play_progression(trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
