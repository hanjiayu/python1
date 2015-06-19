class Student(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
