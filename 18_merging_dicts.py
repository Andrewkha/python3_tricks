xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

zs = {}
zs.update(xs)
zs.update(ys)

print(zs)

# another option but for 2 dicts only
zs = dict(xs, **ys)
print(zs)


# starting Python 3.5
zs = {**xs, **ys}
print(zs)

def test(**kwargs):
    print(kwargs)

test(name='Hello', action='Go west')
