import math
import random

from brain_games.play import (ask_game_question, get_game_answer, check_answer,
                              tell_bye_on_wrong_answer, congratulate)
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def is_prime(number):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    if number % 2 == 0 or number <= 1:
        return False

    if number == 2:
        return True

    root = int(math.sqrt(number)) + 1

    for div in range(3, root, 2):
        if number % div == 0:
            return False
    return True


def play_prime(user, trials_count):
    ask_game_question(
        'Answer "yes" if given number is prime. Otherwise answer "no".')
    answer_mapping = {True: "yes", False: "no"}

    trials = 0
    while trials < trials_count:
        number = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        ask_game_question(f"Question: {number}")
        answer = get_game_answer()
        correct_answer = answer_mapping.get(is_prime(number))

        if check_answer(answer=answer, correct_answer=correct_answer):
            trials += 1
        else:
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
