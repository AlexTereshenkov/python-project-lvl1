import math
import random

from brain_games.play import play_flow
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


def play_prime(trials_count):
    answer_mapping = {True: "yes", False: "no"}

    game_data = []
    for i in range(trials_count):
        number = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        game_data.append((number, answer_mapping.get(is_prime(number))))

    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_flow(question, game_data)
