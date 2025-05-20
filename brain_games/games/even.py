import random
from brain_games.scripts.engine import run_game

GAME_LOGIC = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
	number = random.randint(1, 100)
	question = str(number)
	answer = 'yes' if number % 2 == 0 else 'no'
	return question, answer


def run():
	run_game(GAME_LOGIC, generate_question)





















