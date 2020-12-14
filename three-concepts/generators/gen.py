# gen.py

# in Python there is always
#   ^ top-level syntax or function, and
#   ^ underscore method
#
# top level syntax, function -> underscore method
#   x()                             __call__

from time import sleep


def add1(x, y):
    return x + y


class Adder:
    def __call__(self, x, y):
        return x + y


add2 = Adder()


# add1 is much readable(simpler)  than add2

# This is original IDEA of the compute() function
def compute_x():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv


# class Compute:
#     def __call__(self):
#         rv = []
#         for i in range(10):
#             sleep(.5)
#             rv.append(i)
#         return rv

# Compute = Compute()
# BUT it takes more memory or/and storage
# BELOW scenario is using one unit of memory at one of the time (lesser
# memory/storage required)
# BUT need in simpler expression -> using generator expression

class Compute_x:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv


# Instead above
# Finally the following is the compute() in generator formulation is much simpler
# expression rather than the compute() above
# This is a core concept behind a generator
# How to use generator and yield:
# https://realpython.com/introduction-to-python-generators/
# Common use case of generators is to work with data streams or large files,
# like CSV files

def compute():
    for i in range(10):
        sleep(.5)
        yield i


for val in compute():
    print(val)


# for x in xs:
#     pass

# x1 = iter(xs)     -> __iter__
# while True:
#     x = next(x1)  -> __next__


# The following example shows how to use  APIs
# we'd ideally want to have some interleaving between the user code and the library code
# for the generator or the co-routine, caller enters generator and
# ask for values the generator to run but caller can have this interleaving
#   - user code runs
#   - ask the generator for value
#   - the generator runs it's code yields back to the user code
#   - the user code does whatever at once
#   - it goes back to the generator ask for the value
#   - this is interleaving of two pieces of code :: user code and library code
# the different with subroutine which has single entry point and single exit point
# subroutine is run done and return

def first():
    print('first()')


def second():
    print('second()')


def last():
    print('last()')


class Api:
    def run_this_first(self):
        first()

    def runt_this_second(self):
        second()

    def run_this_last(self):
        last()


# 'yield' has no value but control back to the caller and guarantee the functions are executed in sequential
# generator forces that sequencing on you and it forces that sequencing because the generator is a KO routine
# that allows it's interleaving between two types of code - user code and library code
def api():
    first()
    yield
    second()
    yield
    last()


api()
