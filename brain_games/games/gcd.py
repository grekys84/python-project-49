import random
from math import gcd
from brain_games.scripts.engine import run_game

GAME_LOGIC = 'Find the greatest common divisor of given numbers.'


def generate_question():
	number_first = random.randint(1, 100)
	number_second = random.randint(1, 100)
	question = f"{number_first} {number_second}"
	answer = gcd(number_first, number_second)
	return question, answer


def run():
	run_game(GAME_LOGIC, generate_question)

