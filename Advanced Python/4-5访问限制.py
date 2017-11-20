class Person(object):
    def __init__(self, name, score):
        self.name=name
        self.__score=score

p = Person('Bob', 59)

print p.name
try:
    print p.__score
except AttributeError:
    print"attributeerror"