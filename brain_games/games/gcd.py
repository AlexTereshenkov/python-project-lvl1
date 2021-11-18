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
        game_data.append((f"{number1} {number2}", math_gcd(number1, number2)))

    return game_data
