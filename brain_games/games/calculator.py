import operator
import random

from brain_games.play import play_flow
from brain_games.configs import NUMBERS_MIN, NUMBERS_MAX


def play_calculator(trials_count):
    game_data = []
    for i in range(trials_count):
        number1, number2 = random.randint(NUMBERS_MIN,
                                          NUMBERS_MAX), random.randint(
                                              NUMBERS_MIN, NUMBERS_MAX)
        operations_mapping = {
            "-": operator.sub,
            "+": operator.add,
            "*": operator.mul,
        }
        operation = random.choice(tuple(operations_mapping))
        correct_answer = operations_mapping.get(operation)(number1, number2)
        game_data.append((f"{number1} {operation} {number2}", correct_answer))

    question = 'What is the result of the expression?'
    play_flow(question, game_data)
