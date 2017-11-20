# -*- coding: UTF-8 -*-
class Person(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
# 实例的方法就是在类中定义的函数，__init__是一个特殊的实例方法，用来定义实例的属性
# 而get_name是用来对实例调用
p1 = Person('Bob')
# 用了__init__(self, name):
# 如果是self.name可以再外部直接调用p1.name，但如果是self.__name，就要调用函数得到值
print p1.get_name()
# 调用get_name(self):
# 在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，
# 这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。

