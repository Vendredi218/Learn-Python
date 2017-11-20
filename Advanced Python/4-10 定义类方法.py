# -*- coding: UTF-8 -*-
# 和属性类似，方法也分实例方法和类方法。
# 在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

class Person(object):
    __count = 0
    @classmethod
    # 通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。
    # 类方法的第一个参数将传入类本身，通常将参数名命名为 cls，
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()