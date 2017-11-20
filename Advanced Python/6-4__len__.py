# -*- coding: UTF-8 -*-
class Fib(object):
    def __init__(self, num):
        a=0
        b=1
        self.numbers = []
        for n in range(num):
            self.numbers.append(a)
            s=a+b
            a=b
            b=s
    # self.numbers这个属性当做fib数列内容

    def __str__(self):
        return str(self.numbers)

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)


# class Fib(object):
#     def __init__(self, num):
#         a=0
#         b=1
#         L=[]
#         for n in range(num):
#             L.append(a)
#             s=a+b
#             a=b
#             b=s
#         self.numbers=L
#
#     def __str__(self):
#         return str(self.numbers)
#
#     def __len__(self):
#         return len(self.numbers)
#
# f = Fib(10)
# print f
# print len(f)