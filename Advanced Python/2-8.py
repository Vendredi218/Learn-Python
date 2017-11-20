def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

f = calc_sum([1, 2, 3, 4])
print f()

def calc_prod(lst):
    def lazy_prod():
        return reduce(lambda x,y:x*y,lst,2)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print f()