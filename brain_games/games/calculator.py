import operator
import random

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT
from brain_games.constants import QUESTION_GAME_CALCULATOR


def get_calculator_data():
    game_data = []
    for i in range(TRIALS_COUNT):
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        operations_mapping = {
            "-": operator.sub,
            "+": operator.add,
            "*": operator.mul,
        }
        operation = random.choice(tuple(operations_mapping))
        correct_answer = operations_mapping.get(operation)(number1, number2)
        game_data.append((f"{number1} {operation} {number2}", correct_answer))

    return (QUESTION_GAME_CALCULATOR, game_data)
