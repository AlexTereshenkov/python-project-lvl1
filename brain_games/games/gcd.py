import random
from math import gcd

from brain_games.play import play_flow
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def play_gcd(trials_count):
    game_data = []
    for i in range(trials_count):
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        game_data.append((f"{number1} {number2}", gcd(number1, number2)))

    question = 'Find the greatest common divisor of given numbers.'
    play_flow(question, game_data)
