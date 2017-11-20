def is_odd(x):
    print x % 2 == 1
filter(is_odd, [1, 4, 6, 7, 9, 12, 17])

def is_odd(x):
    return x % 2 == 1
print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])

a='1234abc'
print a.strip('12')
print a.strip('34')
print a

