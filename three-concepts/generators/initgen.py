# initial gen.py

# thought that mental model is often very limited
# Python there is always:
#   ^ top-level syntax or function, and
#   ^ underscore method
#
# top level syntax, function -> underscore method
#
# what we often mean by eager the idea is
# this function irrespective of what you actually care about
# in this computation which always takes the exact amount of memory and the
# exact same amount of time

from time import sleep


def add1(x, y):
    return x + y


class Adder:
    def __init__(self):
        self.z = 0

    def __call__(self, x, y):
        self.z += 1
        return x + y + self.z


add2 = Adder()


def compute():
    rv = []
    for i in range[10]:
        sleep(.5)
        rv.append(i)
    return rv


class Compute:
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


for val in Compute():
    print(val)

compute = Compute()
