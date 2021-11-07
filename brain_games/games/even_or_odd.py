import random

from brain_games.play import play_flow
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def is_even(number):
    return not number % 2


def play_even_or_odd(trials_count):
    answer_mapping = {True: "yes", False: "no"}
    game_data = []
    for i in range(trials_count):
        number = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        game_data.append((number, answer_mapping.get(is_even(number))))
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_flow(question, game_data)
