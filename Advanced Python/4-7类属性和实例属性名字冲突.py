# -*- coding: UTF-8 -*-
class Person(object):

    __count = 0

    def __init__(self, name):
        self.name=name
        Person.__count=Person.__count+1
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')
p2.__count=123
print p2.__count
del p2.__count
print p2.__count
# 可以实例 p2.类属性，也可以类名称Person.类属性
# print Person.__count



# 原因是 p1.address = 'China'并没有改变 Person 的 address，而是给 p1这个实例绑定了实例属性address ，对p1来说，它有一个实例属性address（值是'China'），而它所属的类Person也有一个类属性address，所以:
# 访问 p1.address 时，优先查找实例属性，返回'China'。
#
# 访问 p2.address 时，p2没有实例属性address，但是有类属性address，因此返回'Earth'。
#
# 可见，当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。