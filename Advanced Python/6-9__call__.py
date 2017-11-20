# -*- coding: UTF-8 -*-


class Fib(object):

    def __call__(self, num):
        a = 0
        b = 1
        self.numbers = []
        for n in range(num):
            self.numbers.append(a)
            a,b=b,a+b
        return self.numbers

f = Fib()
print f(10)

# f是一个实例，call函数调用