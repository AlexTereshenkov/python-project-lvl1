import random

from brain_games.play import (
    ask_game_question, get_game_answer, check_answer,
    tell_bye_on_wrong_answer, congratulate)

def is_even(number):
    return not number % 2


def play_even_or_odd(user, trials_count):
    ask_game_question('Answer "yes" if the number is even, otherwise answer "no".')
    answer_mapping = {True: "yes", False: "no"}

    trials = 0
    while trials < trials_count:
        # keeping the number small for user convenience
        number = random.randint(0, 100)
        ask_game_question(f"Question: {number}")
        answer = get_game_answer()
        correct_answer = answer_mapping.get(is_even(number))

        if check_answer(answer=answer, correct_answer=correct_answer):
            trials += 1
        else:
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
