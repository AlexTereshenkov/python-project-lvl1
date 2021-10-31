import random

from brain_games.play import (ask_game_question, get_game_answer, check_answer,
                              tell_bye_on_wrong_answer, congratulate, get_user,
                              welcome_user)
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
    user = get_user()
    welcome_user(user)

    ask_game_question('What number is missing in the progression?')

    trials = 0
    while trials < trials_count:
        progression = get_progression()
        # note that we can't hide the first or the last element in the
        # progression because user doesn't know the original length of
        # the sequence
        random_position = random.randint(1, len(progression) - 2)
        correct_answer = progression[random_position]
        progression[random_position] = ".."

        ask_game_question(f"Question: {' '.join(progression)}")
        answer = get_game_answer()

        if check_answer(answer=answer, correct_answer=correct_answer):
            trials += 1
        else:
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
