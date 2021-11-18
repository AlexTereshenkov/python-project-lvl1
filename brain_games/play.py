import prompt


def play(game):
    question, game_data = game.QUESTION, game.get_data()

    print("Welcome to the Brain Games!")
    user = prompt.string('May I have your name? ')
    print(f"Hello, {user}!")
    print(question)

    for question_value, correct_answer in game_data:
        print(f"Question: {question_value}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            return

    print(f"Congratulations, {user}!")
