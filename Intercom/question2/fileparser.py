import json
from customer import Customer

class FileParser:

	@staticmethod
	def readFile(file_name):
		result = []
		with open(file_name) as whole_file:
			for line in whole_file:
				result.append(line)
		return result

	@staticmethod
	def parseCustomerFile(file_lines):
		customers = []

		for line in file_lines:

			try:
				customer_json = json.loads(line)
			except ValueError:
				continue

			if FileParser.isValidJson(customer_json):
				name = customer_json["name"]
				user_id = customer_json["user_id"]
				latitude = customer_json["latitude"]
				longitude = customer_json["longitude"]

				customer = Customer(user_id, name, latitude, longitude)
				customers.append(customer)

		return customers

	@staticmethod
	def isValidJson(customer_json):
		return FileParser.isFloat(customer_json.get('latitude')) and customer_json.get('user_id') and customer_json.get('name') and FileParser.isFloat(customer_json.get('longitude'))

	@staticmethod
	def isFloat(value):
		if value is None:
			return False
		try:
			float(value)
			return True
		except ValueError:
			return False
