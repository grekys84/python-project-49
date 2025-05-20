import random
from brain_games.scripts.engine import run_game

GAME_LOGIC = "What is the result of the expression?"


def generate_question():
	number_first = random.randint(1, 100)
	number_second = random.randint(1, 100)
	operation = random.choice(['+', '-', '*'])
	question = f"{number_first} {operation} {number_second}"
	answer = eval(question)
	return question, answer


def run():
	run_game(GAME_LOGIC, generate_question)




