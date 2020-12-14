# library.py

# How powerful the data model protocol is illustrated
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


# class Base1:
#     def foo1(self):
#         return 'foo1'


# class Base:
#     def foo(self):
#         return self.bar()


# # old_bc = __build_class__
# # def my_bc(*a, **kw):
# #     print('my buildclass->', a, kw)
# #     return old_bc(*a, **kw)
# # import builtins
# # builtins.__build_class__ = my_bc

# old_bc = __build_class__
# def my_bc(fun, name, base=None, **kw):
#     if base is Base:
#         print('chek if bar method defined')
#     if base is not None:
#         return old_bc(fun, name, **kw)

# import builtins
# builtins.__build_class__ = my_bc

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'Base' and not 'bar' in body:
            raise TypeError("bad user class")
        # print('BaseMeta.__new__', cls, name, bases, body)
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init__subclass(self, *a, **kw):
        print('init_subclass', a, kw)
        return super().__init_subclass__(cls, *a, **kw)
