#  Iterator
class SingleClassRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


#  The same but with generator
def repeater(value):
    while True:
        yield value


#  this will do an infinite Hello print
# for x in repeater('Hello'):
#     print(x)

def repeat_3_times(value):
    yield value
    yield value
    yield value


def repeat_1_time(value):
    yield value


for x in repeat_3_times('Hi'):
    print(x)


for x in repeat_1_time('Cool'):
    print(x)


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


for x in bounded_repeater('Hello', 3):
    print(x)


#  refactor bounded repeater
def bounded_repeater1(value, repeats):
    for i in range(repeats):
        yield value


#  Generator expressions
iterator = ('Fuck' for i in range(3))
for x in iterator:
    print(x)

# Filtering values
even_squares = (x * x for x in range(10) if x % 2 == 0)