# initial dec.py

from time import time


def timer(func):
    def f(x, y=10):
        before = time()
        rv = func(x, y)
        after = time()
        print('elapsed', after - before)
        return rv

    return f


@timer
def add(x, y=10):
    return x + y


# add = timer(add) => instead, it uses decorators @timer

@timer
def sub(x, y=10):
    return x - y


# sub = timer(sub) => instead, it uses decorators @timer


print('add(10)', add(10))
print('add(20, 30)', add(20, 30))
print('add("a", "b")', add("a", "b"))
print('sub(10)', sub(10))
print('sub(20, 30)', sub(20, 30))


# **** below is first idea and it's improved as above ****
# def timer(func, x, y=10):
#     before = time()
#     rv = func(x, y)
#     after = time()
#     print('elapsed', after - before)
#     return rv
#
#
# def add(x, y=10):
#     return x + y
#
#
# def sub(x, y=10):
#     return x - y
#
#
# print('add(10)', timer(add, 10))
# print('add(20, 30)', timer(add, 20, 30))
# print('add("a", "b")', timer(add, "a", "b"))
# print('sub(10)', sub(10))
# print('sub(20, 30)', sub(20, 30))
