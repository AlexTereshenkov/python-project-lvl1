import random
from math import gcd as math_gcd

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_data():
    game_data = []
    for i in range(TRIALS_COUNT):
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        question = f"{number1} {number2}"
        answer = math_gcd(number1, number2)
        game_data.append((question, answer))

    return game_data
