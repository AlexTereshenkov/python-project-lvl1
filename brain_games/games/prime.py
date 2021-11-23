import math
import random

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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


def get_data():
    answer_mapping = {True: "yes", False: "no"}

    game_data = []
    for i in range(TRIALS_COUNT):
        number = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        question = number
        answer = answer_mapping.get(is_prime(number))
        game_data.append((question, answer))

    return game_data
