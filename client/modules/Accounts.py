# -*- coding: utf-8-*-
import re
import yaml
import os 
from client import jasperpath
from client.conversation import Conversation


WORDS = ["LOG", "IN", "OUT", "EXIT", "SIGN", "OFF", "BYE"] 


def handle(text, mic, profile):
	match = re.search('(?<=login ).*', text)
	if match is not None:
		user = match.group()
		new_configfile = jasperpath.config(user + '.yml')
		if os.path.exists(new_configfile):
			with open(new_configfile, "r") as f:
				config = yaml.safe_load(f)
			conversation = Conversation()
        		conversation.setProfile("JASPER", mic, config)
			mic.say("Welcome " + user)
		else:
			mic.say("Error, user not found")
	elif text == "logout":
		new_configfile = jasperpath.config('configs.yml')
		with open(new_configfile, "r") as f:
			config = yaml.safe_load(f)
		conversation = Conversation()
		conversation.setProfile("JASPER", mic, config)
		mic.say("Bye" + profile['first_name'])
def isValid(text):
	return bool(re.search(r'(login|logout)', text, re.IGNORECASE))
