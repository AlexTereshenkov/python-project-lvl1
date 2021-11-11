import random
from math import gcd

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT
from brain_games.constants import QUESTION_GAME_GCD


def get_gcd_data():
    game_data = []
    for i in range(TRIALS_COUNT):
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        game_data.append((f"{number1} {number2}", gcd(number1, number2)))

    return (QUESTION_GAME_GCD, game_data)
