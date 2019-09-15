name = 'Bob'
errno = 25456412145

# 1 old style
print('Hello, %s' % name)
print('%x' % errno) # hex
print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno})

# 2 – “New Style” String Formatting
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))

# 3 – Literal String Interpolation (Python 3.6+)
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
print(f"Hey {name}, there's a {errno:#x} error!")

# 4 – Template Strings
from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)

templ_string = 'Hey $name, there is a $error error!'
Template(templ_string).substitute(name=name, error=hex(errno))
