import unittest
from fileparser import *

class parseCustomerTest(unittest.TestCase):

	def testParseCustomerFile(self):
		input_lines = []
		customers = FileParser.parseCustomerFile(input_lines)
		self.assertEqual(len(customers), 0)

		input_lines = ["{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \"Christina McArdle\", \"longitude\": \"-6.043701\"}",
						"{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \"Christina McArdle\", \"longitude\": \"-6.043701\"}"]
		customers = FileParser.parseCustomerFile(input_lines)
		self.assertEqual(len(customers), 2)

	def testEmpty(self):
		file_lines = []
		customers = FileParser.parseCustomerFile(file_lines)
		self.assertEqual(len(customers), 0)

	def testValidJson(self):
		json_one = "{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \"Christina McArdle\", \"longitude\": \"-6.043701\"}"
		self.assertTrue(FileParser.isValidJson(json.loads(json_one)))

		json_two = "{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \"Christina McArdle\"}"
		self.assertFalse(FileParser.isValidJson(json.loads(json_two)))	

	def testIsFloat(self):
		float_one = "13545345.556"
		self.assertTrue(FileParser.isFloat(float_one))

		float_two = ""
		self.assertFalse(FileParser.isFloat(float_two))		

		float_three = "abasdfa"
		self.assertFalse(FileParser.isFloat(float_three))		

		float_four = "1423"
		self.assertTrue(FileParser.isFloat(float_four))		

		float_five = "1234.234asdfasd"
		self.assertFalse(FileParser.isFloat(float_five))		

def main():
    unittest.main()

if __name__ == '__main__':
    main()