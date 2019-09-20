def integers():
    for i in range(1, 9):
        yield i


def squares(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squares(integers()))
print(list(chain))

#  with generator expressions
integers_ = range(8)
squared = (i * i for i in integers_)
negated_ = (-i for i in squared)

