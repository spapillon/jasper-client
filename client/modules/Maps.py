# -*- coding: utf-8-*-
import random
import re

WORDS = ["MAPS", "DIRECTIONS", "FROM", "TO"]

def handle(text, mic, profile):
	request = {}
	match = re.search('(?<=from ).*?(?=(to|by|$))', text)
	if match is None:
 		request['from'] = profile['home']
	else:
		request['from'] = match.group()
	
	match = re.search('(?<=to ).*?(?=(from|by|$))', text)
	if match is None:
		request['to'] = "ERROR COULD NOT FIND DESTINATION"
	else:
		request['to'] = match.group()
	
	match = re.search('(?<=by ).*?(?=(from|to|$))', text)
	if match is None: 
		request['by'] = profile['default_transport']
	else:
		request['by'] = match.group()
	
	mic.say(str(request))

	
def isValid(text):
	return bool(re.search(r'\b(directions?|maps)', text, re.IGNORECASE))
