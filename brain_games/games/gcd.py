import random
from fractions import gcd

from brain_games.play import (ask_game_question, get_game_answer, check_answer,
                              tell_bye_on_wrong_answer, congratulate)
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def play_gcd(user, trials_count):
    ask_game_question('Find the greatest common divisor of given numbers.')

    trials = 0
    while trials < trials_count:
        # keeping the number small for user convenience
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
