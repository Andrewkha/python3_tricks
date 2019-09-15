def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hello!'


print(greet())


# Applying multiple decorators
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@strong
@emphasis
def greet():
    return 'Hello!'

print(greet())

# Decorators accepting arguments
# Here’s a trace decorator that logs function
# arguments and results during execution time:

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

print(say('Jane', line='Coo-coo'))

# Applying functools.wraps to the wrapper closure returned by the
# decorator carries over the docstring and other metadata of the input
# function:

import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'

print(greet.__name__)
print(greet.__doc__)