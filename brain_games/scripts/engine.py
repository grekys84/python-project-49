from brain_games.cli import welcome_user


def run_game(game_logic, question_generator):
    name = welcome_user()
    print(game_logic)
    for _ in range(3):
        question, correct_answer = question_generator()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')