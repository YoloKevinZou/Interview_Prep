from eventcollection import EventCollection
from event import Event

def main():

	input_text = {
					"events": [
					  {
					    "occasion": "Birthday party",
					    "invited_count": 120,
					    "year": 2016,
					    "month": 2,
					    "day": 14
					  },
					  {
					    "occasion": "Technical discussion",
					    "invited_count": 23,
					    "year": 2016,
					    "month": 11,
					    "day": 24
					  },
					  {
					    "occasion": "Press release",
					    "invited_count": 64,
					    "year": 2015,
					    "month": 12,
					    "day": 17,
					    "cancelled": True
					  },
					  {
					    "occasion": "New year party",
					    "invited_count": 55,
					    "year": 2016,
					    "month": 1,
					    "day": 1
					  }
					]
				 }

	events = input_text["events"]
	event_collection = EventCollection()
	for event in events:
		occasion = event["occasion"]
		invited_count = event["invited_count"]
		year = event["year"]
		month = event["month"]
		day = event["day"]
		event_collection.addEvent(Event(occasion,invited_count,year,month,day))

	print(event_collection)

if __name__ == "__main__": main()
