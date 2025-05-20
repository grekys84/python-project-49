import random
from brain_games.scripts.engine import run_game

GAME_LOGIC = "What number is missing in the progression?"


def generate_question():
	random_number = random.randint(1, 10)
	random_step = random.randint(0, 5)
	progression = []
	for i in range(10):
		random_step = random_step + random_number
		progression.append(random_step)
	random_index = random.randint(0, len(progression) - 1)
	answer = progression.pop(random_index)
	progression.insert(random_index, '..')
	question = progression
	return question, answer


def run():
	run_game(GAME_LOGIC, generate_question)