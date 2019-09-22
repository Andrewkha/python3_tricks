mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

import json
print(json.dumps(mapping, indent=4, sort_keys=True))

mapping['id'] = {1, 2, 3}
# The classical solution to pretty-printing objects in Python is the builtin
# pprint module.
import pprint
pprint.pprint(mapping)
print(mapping)