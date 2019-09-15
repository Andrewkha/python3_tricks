def yell(text: str):
    return text.upper() + '!'


bark = yell
print(bark('wooof'))


def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)

# callable objects
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
print(plus_3(4))
