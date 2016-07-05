# -*- coding: utf-8-*-
import re
import os
import sys
import shutil
import logging
import signal
import yaml
import argparse

from client import tts, stt, jasperpath, diagnose
from client.conversation import Conversation


WORDS = ["LOG", "IN", "OUT", "EXIT", "SIGN", "OFF", "BYE"] 


def handle(text, mic, profile):
	if text == "login":
		new_configfile = jasperpath.config('profile2.yml')
		with open(new_configfile, "r") as f:
			config = yaml.safe_load(f)
		conversation = Conversation()
        	conversation.setProfile("JASPER", mic, config)
	elif text == "logout":
		new_configfile = jasperpath.config('configs.yml')
		with open(new_configfile, "r") as f:
			config = yaml.safe_load(f)
		conversation = Conversation()
		conversation.setProfile("JASPER", mic, config)
def isValid(text):
	return bool(re.search(r'(login|logout)', text, re.IGNORECASE))
