class ManagedFile:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('03_context_mgr_example.txt') as file:
    file.write('koo-coo')


# option 2 - with decorator
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


# example
class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
        indent.print('coocoo')
    indent.print('hey')


# If you’re looking for another exercise to deepen your understanding,
# try implementing a context manager that measures the execution time
# of a code block using the time.time function. Be sure to try out writing
# both a decorator-based and a class-based variant to drive home
# the difference between the two.

from time import time, sleep


class TimeMeasure:

    def __init__(self):
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        print(f'execution time: {self.end - self.start}')


with TimeMeasure() as measure:
    sleep(5)

@contextmanager
def timer():
    try:
        crt_time = time()
        yield crt_time
    finally:
        print(time() - crt_time)

with timer() as tmr:
    sleep(3)
