# -*- coding: UTF-8 -*-
import functools

sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.upper()))
# 用的是cmp这个参数
sorted_ignore_case = functools.partial(sorted,key=str.upper)
# 如果是str.upper()返回的就是值，而我们要的是返回函数
# key参数的值应该是一个函数，这个函数接收一个参数并且返回一个用于比较的关键字。对复杂对象的比较通常是使用对象的切片作为关键字。
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
