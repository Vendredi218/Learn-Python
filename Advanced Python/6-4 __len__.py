# -*- coding: UTF-8 -*-
class Students(object):
    def __init__(self, *args):
        self.names = args

    def __len__(self):
        return len(self.names)

ss = Students('Bob', 'Alice', 'Tim')
print len(ss)

# 在类的定义里的__xx__函数都是对类的新定义操作
