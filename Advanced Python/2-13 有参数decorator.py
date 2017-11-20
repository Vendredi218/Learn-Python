# -*- coding: UTF-8 -*-
import time,functools


def performance(unit):
    def perf_dec(f):
        @functools.wraps(f)
        # 把原函数的所有必要属性都一个一个复制到新函数上，所以Python内置的functools可以用来自动化完成这个“复制”的任务：
        def fn(*args, **kw):
            t=time.time()
            if unit=='ms':
                t=t*1000
            print 'call '+f.__name__+'()in',t,unit
            return f(*args,**kw)
        return fn
    return perf_dec


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print factorial.__name__

print factorial(10)

