import random

from brain_games.configs import (NUMBERS_MIN, NUMBERS_MAX,
                                 MIN_PROGRESSION_LENGTH,
                                 MAX_PROGRESSION_LENGTH, MIN_PROGRESSION_STEP,
                                 MAX_PROGRESSION_STEP, TRIALS_COUNT)

QUESTION = 'What number is missing in the progression?'


def get_progression(start, step, stop):
    return [str(val) for val in range(start, stop + 1, step)]


def get_data():
    game_data = []

    for i in range(TRIALS_COUNT):
        start = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
        stop = start + step * random.randint(MIN_PROGRESSION_LENGTH,
                                             MAX_PROGRESSION_LENGTH)
        progression = get_progression(start, step, stop)
        random_position = random.randint(0, len(progression) - 1)
        answer = progression[random_position]
        progression[random_position] = ".."
        question = ' '.join(progression)
        game_data.append((question, answer))

    return game_data
