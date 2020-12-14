# python data model:
# see to implement -> write some __function__
# https://docs.python.org/3/reference/datamodel.html
# top-level function or top-lvel syntax - corresponding __
#   x + y       ->  __add__
#   init(x)     ->  __init__
#   repr(x)     ->  __repr__
#   x()         ->  __call__
#
# Three main core  OOP in PYTHON
#   - protocol oriented data model (function) of python
#   - built-in inheritance object in python
#   - object orientation of python
#


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3)  # x² + 2x + 3
p2 = Polynomial(3, 4, 3)  # 3x² + 4x + 3
