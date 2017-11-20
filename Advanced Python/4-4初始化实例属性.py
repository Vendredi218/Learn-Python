# -*- coding: UTF-8 -*-
class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name=name
        self.gender=gender
        self.birth=birth
        for k,v in kw.iteritems():
            setattr(self,k,v)

# extra={'job':'Student'}
# xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', **extra)
# job 关键词参数
# 或者下面这样 job='Student'是关键字参数，就是dic转化来的形式
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# 解释器内部会将**kw拆分成对应的dict.
# setattr()方法接受3个参数：setattr(对象，属性，属性的值)
# setattr(self,k,v)相当于self.k = v
# kw.iteritems()历遍字典kw的所有key和value，分别匹配k，v