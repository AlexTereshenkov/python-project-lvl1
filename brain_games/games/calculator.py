import operator
import random

from brain_games.play import (ask_game_question, get_game_answer, check_answer,
                              tell_bye_on_wrong_answer, congratulate)
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def play_calculator(user, trials_count):
    ask_game_question('What is the result of the expression?')

    trials = 0
    while trials < trials_count:
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        operations_mapping = {
            "-": operator.sub,
            "+": operator.add,
            "*": operator.mul,
        }
        operation = random.choice(tuple(operations_mapping))

        ask_game_question(f"Question: {number1} {operation} {number2}")
        answer = get_game_answer()
        correct_answer = operations_mapping.get(operation)(number1, number2)

        if check_answer(answer=answer, correct_answer=correct_answer):
            trials += 1
        else:
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
