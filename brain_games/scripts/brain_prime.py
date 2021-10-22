#!/usr/bin/env python

from brain_games.play import get_user, welcome_user
from brain_games.games.prime import play_prime
from brain_games.configs import TRIALS_COUNT


def main():
    user = get_user()
    welcome_user(user)
    play_prime(user=user, trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
