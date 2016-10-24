class EventCollection:
	def __init__(self):
		self.events = []

	def addEvent(self, event):
		self.events.append(event)

	def addEvents(self, events):
		self.events = events

	def __str__(self):

		result = ""
		for event in self.events:
			result += str(event)
			result += "\n"

		return result