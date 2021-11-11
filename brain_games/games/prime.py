import math
import random

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT
from brain_games.constants import QUESTION_GAME_PRIME


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


def get_prime_data():
    answer_mapping = {True: "yes", False: "no"}

    game_data = []
    for i in range(TRIALS_COUNT):
        number = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        game_data.append((number, answer_mapping.get(is_prime(number))))

    return (QUESTION_GAME_PRIME, game_data)
