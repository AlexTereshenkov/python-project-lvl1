import random

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT
from brain_games.constants import QUESTION_GAME_EVEN_OR_ODD


def is_even(number):
    return not number % 2


def get_even_or_odd_data():
    answer_mapping = {True: "yes", False: "no"}
    game_data = []
    for i in range(TRIALS_COUNT):
        number = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        game_data.append((number, answer_mapping.get(is_even(number))))
    return (QUESTION_GAME_EVEN_OR_ODD, game_data)
