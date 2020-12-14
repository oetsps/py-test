# dec.py :: decorator

from time import time


# def add(x, y=10):
#     before = time()
#     rv = x + y
#     after = time()
#     print('elapsed', after - before)
#     return x + y

# def timer(func):
#     def f(*args, **kwargs):
#         before = time()
#         rv = func(*args, **kwargs)
#         after = time()
#         print('elapsed', after - before)
#         return rv
#     return f


# high order decorator :: simplistic extension an idea
# this is called closer object duality
#   ^ function return a function
#   ^ where the inner function return to other function
#
# core idea is the decorator syntax could do  replacement easily
# with a wrapper function
# in order to have a programmatic behavior:
#   ^ just add one level function outside
#     that constructs decorator
#   ^ the decorator thing constructs the wrapper
#   ^ the wrapper wraps the function itself

def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            before = time()
            for _ in range(n):
                print('running {.__name__}'.format(f))
                rv = f(*args, **kwargs)
            after = time()
            print('elapsed: ', after - before)
            return rv

        return wrapper

    return inner


@ntimes(3)  # decorator
def add(x, y=10):
    return x + y


@ntimes(4)  # decorator
def sub(x, y=10):
    return x - y


# sub = timer(sub)

print('add(10) -> ', add(10))
print('add(20, 30) -> ', add(20, 30))
print('add("a", "b") -> ', add("a", "b"))
print('sub(10)', sub(10))
print('sub(20, 30)', sub(20, 30))
