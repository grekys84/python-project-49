import random
from brain_games.scripts.engine import run_game

GAME_LOGIC = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True


def generate_question():
	number = random.randint(1, 3571)
	question = f"{number}"
	answer = 'yes' if is_prime(number) else 'no'
	return question, answer


def run():
	run_game(GAME_LOGIC, generate_question)