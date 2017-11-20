# -*- coding: UTF-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.score < s.score:
            return 1
        elif self.score > s.score:
            return -1
        else:
            return cmp(self.name,s.name)


L = [Student('Tim', 99), Student('Bob', 99), Student('Alice', 77)]
print sorted(L)
# __cmp__相当于实例对象相对于原本str或者int的一种比较方式

