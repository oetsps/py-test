# oet
# Data model
# some behaviour that I want to implement -> write some __function__
# this is called data model (double underscore) method
# ref. to https://docs.python.org/3/reference/datamodel.html
# top-level function or top-level syntax -> corresponding __
# to add objects:       x + y   -> __add__
# to initialize object: init x  -> __init__
# to repr object:       repr(x) -> __repr__
# to call the object:   x()     -> __call__
#
# THREE OOP in PYTHON
#   - protocol oriented data model (function) of python
#   - built-in inheritence object in python
#   - object orientation of python
#

# ithe IDEA
# below example => how to compact it
#
#    class Polynomial:
#        pass
#
#    p1 = Polynomial()
#    p2 = Polynomial()
#    p1.coeffs = 1, 2, 3     #  x² + 2x + 3
#    p2.coeffs = 3, 4, 3     # 3x² + 4x + 3



class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass


p1 = Polynomial(1, 2, 3)    # x² + 2x +3
p2 = Polynomial(3, 4, 3)    # 3x² + 4x + 3

