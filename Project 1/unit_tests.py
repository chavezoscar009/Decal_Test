import unittest
import mastermind

class testMastermind(unittest.TestCase):

	def test_wrong_code_length(self):
		cases = [
			(['1', '2', '4', '3'], False),
			(['1', '2', '4', '5', '4'], True),
			(['1', '2'], True),
		]

		for case in cases:
			attempt, expectedOutput = case
			self.assertEqual(mastermind.wrong_code_length(attempt), expectedOutput)

	def test_wrong_characters(self):
		cases = [
			(['1', '2', '4', '3'], False),
			(['b', 'e', 'e', 'p'], True),
			(['m', 'a', 'r', 's'], True),
		]

		for case in cases:
			attempt, expectedOutput = case
			self.assertEqual(mastermind.wrong_characters(attempt), expectedOutput)	


	def test_check_numbers(self):
		cases = [
			(['1', '1', '2', '4'], ['1', '1', '2', '4'], 4),
			(['1', '1', '2', '4'], ['2', '1', '3', '4'], 3),
			(['2', '1', '2', '1'], ['3', '1', '4', '1'], 2),
		]

		for case in cases:
			code, attempt, expectedOutput = case
			self.assertEqual(mastermind.check_numbers(code, attempt), expectedOutput)


	def test_check_order(self):
		cases = [
			(['1', '1', '2', '4'], ['1', '1', '2', '4'], 4),
			(['1', '1', '2', '4'], ['2', '1', '3', '4'], 2),
			(['2', '1', '2', '1'], ['3', '1', '4', '3'], 1),
			(['2', '1', '3', '1'], ['3', '3', '3', '3'], 1)
		]

		for case in cases:
			code, attempt, expectedOutput = case
			self.assertEqual(mastermind.check_order(code, attempt), expectedOutput)

	def test_get_key_pegs(self):
		cases = [
			(4, 4, ["Red", "Red", "Red", "Red"]),
			(3, 2, ["Red", "Red", "White", "Empty"]),
			(1, 1, ["Red", "Empty", "Empty", "Empty"]),
			(2, 2, ["Red", "Red", "Empty", "Empty"]),
			(4, 0, ["White", "White", "White", "White"])
		]

		for case in cases:
			numbers_check, orders_check, expectedOutput = case
			self.assertEqual(mastermind.get_key_pegs(numbers_check, orders_check), expectedOutput)

	

if __name__ == '__main__':
 	unittest.main() 
