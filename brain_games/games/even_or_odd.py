import random

from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX, TRIALS_COUNT

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return not number % 2


def get_data():
    answer_mapping = {True: "yes", False: "no"}
    game_data = []
    for i in range(TRIALS_COUNT):
        question = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        answer = answer_mapping.get(is_even(question))
        game_data.append((question, answer))
    return game_data
