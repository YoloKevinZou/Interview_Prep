class Event:

	def __init__(self, occasion, invited_count, year, month, day):
		self.occasion = occasion
		self.invited_count = invited_count
		self.year = year
		self.month = month
		self.day = day

	def __str__(self):
		return "Occasion: %s \t Invited Count: %s \t Month: %s \t Day: %s \t Year: %s" %(self.occasion, self.invited_count, self.month, self.day, self.year)