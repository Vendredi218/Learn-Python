# -*- coding: UTF-8 -*-
# 我们在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象：
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob', 90)
print p1.get_grade
# 是方法，前面的p1就是调用这个方法的对象，即实例，整句来说就是实例方法
print p1.get_grade()



class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
# 是函数，是实例的一个属性，只不过这里的属性是一个函数对象，即f
print p1.get_grade()