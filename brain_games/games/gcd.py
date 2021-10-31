import random
from math import gcd

from brain_games.play import (ask_game_question, get_game_answer, check_answer,
                              tell_bye_on_wrong_answer, congratulate, get_user,
                              welcome_user)
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def play_gcd(trials_count):
    user = get_user()
    welcome_user(user)

    ask_game_question('Find the greatest common divisor of given numbers.')

    trials = 0
    while trials < trials_count:
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        ask_game_question(f"Question: {number1} {number2}")
        answer = get_game_answer()
        correct_answer = gcd(number1, number2)

        if check_answer(answer=answer, correct_answer=correct_answer):
            trials += 1
        else:
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
