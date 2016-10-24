from customer import Customer
from location import Location
import math

class CustomerCollection:

	distance_threshold = 100 #km according to exercise
	earth_radius = 6371 #km according to wikipedia

	def __init__(self, customers):
		self.customers = customers

	def addCustomer(self, customer):
		self.customers.append(customer)

	def computeDistance(self, locationOne, locationTwo):
		partA = math.sin(self.degreeToRadian(locationOne.latitude)) * math.sin(self.degreeToRadian(locationTwo.latitude))
		partB = math.cos(self.degreeToRadian(locationOne.latitude)) * math.cos(self.degreeToRadian(locationTwo.latitude)) * math.cos(abs(float(locationTwo.longitude) - float(locationOne.longitude)))
		result = self.earth_radius * math.acos(partA + partB)
		return result

	def customersCloseToLocation(self, location):
		result = []

		for customer in self.customers:
			customer_location = Location(customer.latitude, customer.longitude)
			distance = self.computeDistance(location, customer_location)

			if distance <= self.distance_threshold:
				result.append((customer, distance))

		return result

	def degreeToRadian(self, degree):
		return math.radians(float(degree))

	def sortCustomerByUserId(self, customers):
		return sorted(customers, key=self.getKey)

	def getKey(self, customer):
	    return customer[0].user_id

	def getCustomers(self):
		return self.customers