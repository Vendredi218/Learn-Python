class Person(object):
    count=0
    def __init__(self,name):
        self.name=name
        Person.count=Person.count+1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count