import prompt


def check_answer(answer, correct_answer):
    if answer == str(correct_answer):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def play_flow(game_data_getter):
    question, game_data = game_data_getter()

    print("Welcome to the Brain Games!")
    user = prompt.string('May I have your name? ')
    print(f"Hello, {user}!")
    print(question)

    for question_value, correct_answer in game_data:
        print(f"Question: {question_value}")
        user_answer = prompt.string("Your answer: ")

        if not check_answer(answer=user_answer, correct_answer=correct_answer):
            print(f"Let's try again, {user}!")
            return

    print(f"Congratulations, {user}!")
