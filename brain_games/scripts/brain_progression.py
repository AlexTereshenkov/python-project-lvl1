#!/usr/bin/env python

from brain_games.play import get_user, welcome_user
from brain_games.games.progression import play_progression
from brain_games.configs import TRIALS_COUNT


def main():
    user = get_user()
    welcome_user(user)
    play_progression(user=user, trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
