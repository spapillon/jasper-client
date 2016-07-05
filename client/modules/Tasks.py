import re
from client import task_manager

WORDS = ["CLOSE", "NEXT", "SWITCH"]


def handle(text, mic, profile):
    if bool(re.search('close', text)):
        task_manager.TaskManager().closeTask()
    elif bool(re.search('next', text)):
        task_manager.TaskManager().nextTask()
    elif bool(re.search('(?<=switch ).*', text)):
        name = re.search('(?<=switch ).*', text).group()
        task_manager.TaskManager().findTask(name)
    elif bool(re.search('(?<=add ).*', text)):
        name = re.search('(?<=add ).*', text).group()
        task_manager.TaskManager().createTask(name)
    else:
        mic.say("Could not find command")

def isValid(text):
    return bool(re.search(r'(close|next|switch|add)', text))
