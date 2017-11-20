# -*- coding: UTF-8 -*-
# 用装饰器函数把 get/set 方法“装饰”成属性调用：

# @property---这是关键字，固定格式，能让方法当“属性”用。
# @score.setter---前面的"score"是@property紧跟的下面定义的那个方法的名字，"setter"是关键字，
# 这种“@+方法名字+点+setter”是个固定格式与@property搭配使用。


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def get_score(self):
        return self.__score

    @get_score.setter
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

s=Student('wang',88)

print s.get_score
s.set_score=12
print s.get_score

# print s.get_score()
# s.set_score(86)
# print s.get_score()

# 上面那个是把方法名作为了属性，下面那个还是在调用方法