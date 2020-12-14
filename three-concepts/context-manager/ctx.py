# ctx.py
# context manager is a very simple metaphor
# compare the concept in C++ which is called such resources allocation and initialization
#
# context managers have such a clear unambiguous metaphor behind them
#
# below is an example codes in Python which implement metaphor
# with open('ctx.py') as f:
#     pass
# fundamentally there is metaphor idea which have:
#   - some setup action and teardown action
#   - some initial action and final action
#
from sqlite3 import connect


# ****************************************************************************
# in Python there is always high level syntax - function - underscore method
# below example there is pair of __enter__ and __exit__
#       with ctx() as x:
#           pass
#
#        x = ctx().__enter__()
#        try:
#           pass
#       finally:
#           x.__exit__()
# ***************************************************************************


class temptable:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        print('__enter__')
        self.cur.execute('create table points(x int, y int)')

    def __exit__(self, *args):
        print('__exit__')
        self.cur.execute('drop table points')


with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
