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
    _current_task = None

    def createTask(self, name):
        task = Task(name)
        self.addTask(task)

    def addTask(self, task):
        if isinstance(task, Task):
            self._tasks.insert(0, task)
            self._cycle = cycle(self._tasks)
            self.nextTask()
        else:
            print("Tried to append a non Task Object")

    def closeTask(self):
        if self._current_task != None:
            self._current_task.close()
            self._tasks.remove(self._current_task)
            self._cycle = cycle(self._tasks)
            self.nextTask()

    def nextTask(self):
        if len(self._tasks) > 0:
            self._current_task = self._cycle.next()
            self._current_task.focus()
        else:
            self._current_task = None

    def findTask(self, name):
        for task in self._tasks:
            if task.getName() == name:
                self._current_task = task
                self._current_task.focus()

    def executeTask(self, command):
        self._current_task.execute(command)

