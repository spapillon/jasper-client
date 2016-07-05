#!/usr/bin/python
import os
import sys
from task import *
from singleton import Singleton
from itertools import cycle

class TaskManager(object):
    __metaclass__ = Singleton
    _tasks = []
    _cycle = None
    def getTasks(self):
        return self._task

    def addTask(self, task):
        if isinstance(task, Task):
            self._tasks.append(task)
            self._cycle = cycle(self._tasks)
        else:
            print("Tried to append a non Task Object")

    def closeTask(self, task):
        if task not in self._tasks:
            print("Tried to close a task that is not in the Manager")
            return
        task.close()
        self._tasks.remove(task)
        self._cycle = cycle(self._tasks)

    def nextTask(self):
        return self._cycle.next()

    def findTask(self, name):
        for task in self._tasks:
            if task.name == name:
                return task
        return None
