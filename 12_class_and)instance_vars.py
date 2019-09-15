class Dog:
    num_legs = 4 # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


jack = Dog('jack')
jill = Dog('jill')

print(Dog.num_legs)
# print(Dog.name)  # will give an error

Dog.num_legs = 6  # will affect all instances of Dog class
Dog.num_legs = 4  # will affect all instances of Dog class

# to modify num leg for one specific dog only
jack.num_legs = 6

print(jack.num_legs)
print(jill.num_legs)


class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


class BuggyCountedObject:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1 # !!! this is wrong! This
# implementation won’t work because I accidentally “shadowed” the
# num_instance class variable by creating an instance variable of the
# same name in the constructor.