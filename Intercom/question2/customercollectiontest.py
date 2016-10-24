import unittest
from customercollection import CustomerCollection
from customer import Customer
from location import Location

class CustomerCollectionTest(unittest.TestCase):

	def testDegreeToRad(self):
		customers = []
		customer_collection = CustomerCollection(customers)
		degree = 90
		self.assertEqual(round(customer_collection.degreeToRadian(degree), 4), 1.5708)

	def testComputeDistance(self):
		customers = []
		customer_collection = CustomerCollection(customers)
		dublin_office = Location("53.3381985", "-6.2592576")
		distance = customer_collection.computeDistance(dublin_office, dublin_office)
		self.assertEqual(distance, 0)

	def testCustomerCloseToLocation(self):
		
		dublin_office = Location("53.3381985", "-6.2592576")
		customer_one = Customer(12, "Christina McArdle", "52.986375", "-6.043701")
		customer_two = Customer(2, "Ian McArdle", "51.8856167", "-10.4240951")
		customer_three = Customer(1, "Alice Cahill", "51.92893", "-10.27699")
		customer_four = Customer(5, "Nora Dempsey", "53.1302756", "-6.2397222")

		customers = []
		customers.append(customer_one)
		customers.append(customer_two)
		customers.append(customer_three)
		customers.append(customer_four)

		customer_collection = CustomerCollection(customers)

		result = customer_collection.customersCloseToLocation(dublin_office)
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0][0].user_id, 5)


	def testSortByCustomerId(self):
		customer_one = Customer(5, "a", "45.334", "23")
		customer_two = Customer(8, "b", "45.334", "23")
		customer_three = Customer(2, "c", "45.334", "23")
		customer_four = Customer(4, "d", "45.334", "23")
		customer_five = Customer(6, "e", "45.334", "23")

		customers = []
		customers.append((customer_one, 1))
		customers.append((customer_two, 1))
		customers.append((customer_three, 1))
		customers.append((customer_four, 1))
		customers.append((customer_five, 1))
		customer_collection = CustomerCollection([])

		sortedCustomers = customer_collection.sortCustomerByUserId(customers)

		self.assertEqual(sortedCustomers[0][0].user_id, 2)
		self.assertEqual(sortedCustomers[1][0].user_id, 4)
		self.assertEqual(sortedCustomers[2][0].user_id, 5)
		self.assertEqual(sortedCustomers[3][0].user_id, 6)
		self.assertEqual(sortedCustomers[4][0].user_id, 8)

def main():
    unittest.main()

if __name__ == '__main__':
    main()