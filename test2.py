class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printstr(self):
        print(self.name, self.age)