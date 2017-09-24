'''
DISPEVENTS.py

args: POSTCODE
returns: 5 closest events (str)
'''
import requests
import csv

KEY = "2d1a5c7c2b23764d47326156c30bc"
'''
x = "https://api.meetup.com/find/events?&sign=true&photo-host=public&text=chess&only=id"

t = requests.get(x).json()
print(t)
'''

'''
dispEvents
'''
def dispEvents(postcode):
	postcode = str(postcode)
	with open('data.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			if row[0] == postcode:			
				LAT, LON = str(row[1]), str(row[2])
				break

	RADIUS = "100"

	url = "https://api.meetup.com/find/events?&sign=true&photo-host=public&lon=" + LON + "&radius=" + RADIUS + "&lat=" + LAT + "&only=name&key=" + KEY
	idurl = "https://api.meetup.com/find/events?&sign=true&photo-host=public&lon=" + LON + "&radius=" + RADIUS + "&lat=" + LAT + "&only=id&key=" + KEY
	
	r = requests.get(url)
	events = r.json()
	idjson = requests.get(idurl).json()
	ids = []

	numOfEvents = 4
	display = ''
	i = 1
	for event in events[:numOfEvents]:
		display += '#' + str(i) + ': ' + event['name']
		display += '\n'
		i += 1
	for id in idjson[:numOfEvents]:
		ids.append(id['id'])
	
	return (display, ids)
	
'''
RSVP
'''
def RSVP(event_id):
	event_id = str(event_id)
	url = "https://api.meetup.com/2/rsvp/"
	r = requests.post(url, data = {'key': KEY, 'event_id': event_id, 'rsvp': 'yes'})
	
'''
Get event info
'''
def getEventInfo(event_id):
	event_id = str(event_id)
	urlDesc = "https://api.meetup.com/OracleBrisbaneAU/events/243598558?&sign=true&photo-host=public&only=description"
	desc = requests.get(urlDesc).json()['description']
	return("" + desc + "")