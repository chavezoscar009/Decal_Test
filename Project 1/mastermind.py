import random

LENGTH_OF_CODE = 4

ALLOWED_CHARACTERS = ['1', '2', '3', '4']

def generate_code():
	"""
	Returns secret code, which is a randomly generated four-element list of 
	numbers between 1-4.

	>>> generate_code()
	['1', '4', '3', '2']
	>>> generate_code()
	['4', '4', '1', '3']
	>>> generate_code()
	['2', '3', '4', '3']
	"""
	"*** YOUR CODE HERE ***"

def wrong_code_length(code_breaker_attempt):
	"""
	Returns True if the length of the code_breaker_attempt is not the allowed length set
	LENGTH_OF_CODE.

	>>> wrong_code_length(['1', '2', '4', '3'])
	False
	>>> wrong_code_length(['1', '2', '4', '5', '4'])
	True
	>>> wrong_code_length(['1', '2'])
	True
	"""

	"*** YOUR CODE HERE ***"

def wrong_characters(code_breaker_attempt):
	"""
	Returns True if code_breaker_attempt contains characters that are not allowed,
	which is set by ALLOWED_CHARACTERS.

	>>> wrong_code_length(['1', '2', '4', '3'])
	False
	>>> wrong_code_length(['b', 'e', 'e', 'p'])
	True
	>>> wrong_code_length(['m', 'a', 'r', 's'])
	True
	"""

	"*** YOUR CODE HERE ***"

def get_code_breaker_attempt():
	"""
	The code breaker attempts to guess the secret code. This functions returns that
	attempt as a four-element list. This function also checks to make sure if the 
	attempt is valid (the right length and using valid letters). If not, then it
	continues to ask for a valid answer until one is given. 

	"""
	"*** YOUR CODE HERE ***"


def check_numbers(code, code_breaker_attempt):
	""" 
	Checks if colors guessed by the code breaker exist in the secret code. Returns
	the number of correct colors.

	>>> check_numbers(['1', '1', '2', '4'], ['1', '1', '2', '4'])
	4
	>>> check_numbers(['1', '1', '2', '4'], ['2', '1', '3', '4'])
	2
	>>> check_numbers(['2', '1', '2', '1'], ['3', '1', '4', '1'])
	2
	"""

	"*** YOUR CODE HERE ***"



def check_order(code, code_breaker_attempt):
	"""
	Checks if numbers are in the same position as the corresponding number in
	the code. Returns the number of colors in the correct position.

	>>> check_order(['1', '1', '2', '4'], ['1', '1', '2', '4']))
	4
	>>> check_order(['1', '1', '2', '4'], ['2', '1', '3', '4'])
	2
	>>> check_order(['2', '1', '2', '1'], ['3', '1', '4', '3'])
	1
	"""

	"*** YOUR CODE HERE ***" 


def get_key_pegs(numbers_check, order_check):
	"""
	Key pegs returns feedback to code breaker about how much of their code is correct.

	Red: Number is in the right position
	White: Number is in the wrong position
	Empty: Number (or duplicate of number) does not exist in the secret code.
	"""

	"*** YOUR CODE HERE ***"



def give_player_feedback(key_pegs):

	"*** YOUR CODE HERE ***"


MAX_ATTEMPTS = 10

def continue_game_condition(key_pegs, attempts):

	"*** (OPTIONAL) YOUR CODE HERE ***"


def mastermind():

	"*** YOUR CODE HERE ***"

mastermind()