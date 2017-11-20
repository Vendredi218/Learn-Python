class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if isinstance(s,Student):
            return cmp(self.name,s.name)
        else:
            return cmp(self.name,str(s))
#         transfer s into the form of str

B = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
print sorted(B)