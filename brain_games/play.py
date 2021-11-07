import prompt


def get_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(user):
    print(f"Hello, {user}!")
    return


def ask_game_question(question):
    print(question)


def get_user_answer():
    return prompt.string("Your answer: ")


def check_answer(answer, correct_answer):
    if answer == str(correct_answer):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def tell_bye_on_wrong_answer(user):
    print(f"Let's try again, {user}!")


def congratulate(user):
    print(f"Congratulations, {user}!")


def play_flow(question, game_data):
    user = get_user()
    welcome_user(user)
    ask_game_question(question)

    for item in game_data:
        question_value = item[0]
        correct_answer = item[1]
        ask_game_question(f"Question: {question_value}")
        user_answer = get_user_answer()

        if not check_answer(answer=user_answer, correct_answer=correct_answer):
            tell_bye_on_wrong_answer(user)
            return

    congratulate(user)
