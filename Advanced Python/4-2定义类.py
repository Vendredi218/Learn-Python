# -*- coding: UTF-8 -*-
class Person:
    def __init__(self,name):
        self.name=name
# self是一个对象，是当前类的实例instance，Person是class类
xiaoming = Person("xiaoming")
xiaohong = Person("xiaohong")

print xiaoming.name
print xiaoming
print xiaohong
print xiaoming==xiaohong