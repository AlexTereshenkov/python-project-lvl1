import random

from brain_games.play import play_flow
from brain_games.configs import (NUMBERS_MIN, NUMBERS_MAX,
                                 MIN_PROGRESSION_LENGTH,
                                 MAX_PROGRESSION_LENGTH, MIN_PROGRESSION_STEP,
                                 MAX_PROGRESSION_STEP)


def get_progression():
    start = random.randint(NUMBERS_MIN, NUMBERS_MAX)
    step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    stop = start + step * random.randint(MIN_PROGRESSION_LENGTH,
                                         MAX_PROGRESSION_LENGTH)
    return [str(val) for val in range(start, stop + 1, step)]


def play_progression(trials_count):
    game_data = []

    for i in range(trials_count):
        progression = get_progression()
        # note that we can't hide the first or the last element in the
        # progression because user doesn't know the original length of
        # the sequence
        random_position = random.randint(1, len(progression) - 2)
        correct_answer = progression[random_position]
        progression[random_position] = ".."

        game_data.append((f"{' '.join(progression)}", correct_answer))

    question = 'What number is missing in the progression?'
    play_flow(question, game_data)
