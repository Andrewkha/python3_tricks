from collections import defaultdict
dd = defaultdict(list)

dd['dogs'].append('sdsdsd')

print(dd)
print(dd['dogs'])
print(dd['cats'])

s = defaultdict(lambda: 'hernya')
print(s['sddd'])


# To compare two tuples, Python compares the items stored at index
# zero first. If they differ, this defines the outcome of the comparison.
# If they’re equal, the next two items at index one are compared, and so
# on.

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(xs.items())
print(type(xs.items()))
print(sorted(xs.items()))


# Let’s say you wanted to get a sorted representation of a dictionary
# based on its values. To get this result you could use the following key
# func which returns the value of each key/value pair by looking up the
# second element in the tuple:

print(sorted(xs.items(), key=lambda x: x[1]))

# the same with itemgetter
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
