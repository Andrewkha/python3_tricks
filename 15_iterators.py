# 2 classes


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


# repeater = Repeater('Hello')
# for item in repeater:
#     print(item)


#  Single class
class SingleClassRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


# experimenting - returning the letters from the word
class WordIterator:

    def __init__(self, value):
        self.value = value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.value):
            next_char = self.value[self.current]
            self.current += 1
            return next_char
        else:
            raise StopIteration


name = 'Andrey'
iter_ = WordIterator(name)
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
# print(next(iter_))
#
# for char in range(0, len(name)):
#     print(next(iter_))

for char in iter_:
    print(char)


#  Bounded repeater
class BoundedRepeater:
    def __init__(self, value, max_count):
        self.value = value
        self.max_count = max_count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_count:
            self.current += 1
            return self.value
        else:
            raise StopIteration


iter2 = BoundedRepeater('Hello', 5)
for val in iter2:
    print(val)
