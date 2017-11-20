# -*- coding: UTF-8 -*-
class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    __slots__ = ('score')

    def __init__(self, name, gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score

# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的。
# 除非在子类中也定义__slots__，就像答案中一样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
