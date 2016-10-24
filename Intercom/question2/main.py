from fileparser import FileParser
from location import Location
from customercollection import CustomerCollection

def main():

	file_name = 'customers.txt'
	file_lines = FileParser.readFile(file_name)
	dublin_office = Location("53.3381985", "-6.2592576")

	all_customers_collection = CustomerCollection(FileParser.parseCustomerFile(file_lines))

	invited_customers = all_customers_collection.customersCloseToLocation(dublin_office)
	
	for customer in all_customers_collection.sortCustomerByUserId(invited_customers):
		print("UserId: " + str(customer[0].user_id) + "\t Name: " + customer[0].name + "\t Distance: " + str(customer[1]))


if __name__ == "__main__": main()
