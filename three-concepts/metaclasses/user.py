# user.py

# How powerful the data model protocol is ilustrated
# in the following metaclasses expression ....
# Three features of metaclasses:
#   ^ decorators
#   ^ generators
#   ^ context manager
#
#
# Python is protocol oriented data model language
# the following away to check any possibility coding could be broken
# due to naming method/function using both lib and user codes


from library import Base

# assert hasattr(Base1, 'foo'), "you broke it, you fool"
# class Derived1(Base1):
#     def bar1(self):
#         return self.foo1()


class Derived(Base):
    def bar(self):
        return 'bar'
