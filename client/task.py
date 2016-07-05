
class Task(object):
    _name = ""
    def __init__(self, name):
        self._name = name
    
    def open(self):
        pass
    
    def close(self):
        pass

    def focus(self):
        print "%s now in Focus" % self._name

    def execute(self, command):
        pass

    def getName(self):
        return self._name
