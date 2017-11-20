def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()

def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return lambda : i*i
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f())
    return fs
f1, f2, f3 = count()
print f1, f2, f3


def count():
    fs = []
    for i in range(1, 5):
        def f(m=i):
             return m*m
        fs.append(f)
    return fs
f1, f2, f3,f4 = count()
print f1(),f2(),f3(),f4()