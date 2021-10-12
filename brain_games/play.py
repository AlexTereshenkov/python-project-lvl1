import prompt
import random


def get_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(user):
    print(f"Hello, {user}!")
    return


def is_even(number):
    return not number % 2


def play_even_or_odd(user, trials_count):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_mapping = {True: "yes", False: "no"}

    trials = 0
    while trials < trials_count:
        # keeping the number small for user convenience
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        correct_answer = answer_mapping.get(is_even(number))

        if answer == correct_answer:
            print("Correct!")
            trials += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user}!")
            return

    print(f"Congratulations, {user}!")
