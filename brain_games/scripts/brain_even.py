#!/usr/bin/env python

from brain_games.play import get_user, welcome_user, play_even_or_odd

# number of times user must answer correctly
TRIALS_COUNT = 3


def main():
    user = get_user()
    welcome_user(user)
    play_even_or_odd(user=user, trials_count=TRIALS_COUNT)


if __name__ == "__main__":
    main()
