import meetupAPI as mapi

def debug():
	print(mapi.dispEvents(4031))
	mapi.RSVP("243598558")
	print(mapi.dispEvents("243598558"))
	
def flow():
	#get postcode
	sms = input()
	evNames, evIDs = mapi.dispEvents(sms)
	print("-Welcome to Muster, An event service for rural communities.\n-Events near " + sms + "\n" + evNames + "-Type INFO \043 for more information or RSVP \043 to r.s.v.p.")
	#get rsvp/information
	sms = input()
	selected_event_id = evIDs[int(sms[-1])]
	command = sms[0]
	if command == 'r': #rsvp
		print('To confirm your rsvp please enter your name')
		name = input()
		print('Thanks for your rsvp, ' + name + ", We'll keep you updated!")
		mapi.RSVP(selected_event_id)
	else: #info
		print(mapi.getEventInfo(selected_event_id))
		
	

if __name__ == "__main__":
	flow()
	
