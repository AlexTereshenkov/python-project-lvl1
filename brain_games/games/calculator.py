import operator
import random

from brain_games.play import (
    ask_game_question, get_game_answer, check_answer,
    tell_bye_on_wrong_answer, congratulate)


def play_calculator(user, trials_count):
    ask_game_question('What is the result of the expression?')
    
    trials = 0
    while trials < trials_count:
        # keeping the number small for user convenience
        number1, number2 = random.randint(0, 100), random.randint(0, 100)
        operations_mapping = {
            "-": operator.sub, 
            "+": operator.add,
            "*": operator.mul,
        }
        operation = random.choice(tuple(operations_mapping)) 

        ask_game_question(f"Question: {number1} {operation} {number2}")        
        answer = get_game_answer()
        correct_answer = operations_mapping.get(operation)(number1, number2)

        if check_answer(answer=answer, correct_answer=correct_answer):
            trials += 1
        else:
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
