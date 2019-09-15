from collections import namedtuple

# Car = namedtuple('Car', 'color mileage')
Car = namedtuple('Car', 'color mileage')

# or
Bike = namedtuple('Bike', [
    'color',
    'mileage',
])

my_car = Car('red', 4545)
print(my_car)

color, mileage = my_car
print(color, mileage)
print(*my_car)

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 1234)
print(c.hexcolor())

# adding fields
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

# _asdict() helper method. It returns the contents of a namedtuple as a dictionary:
print(my_car._asdict())
import json
json.dumps(my_car._asdict())

# _replace() function. It creates a (shallow)
# copy of a tuple and allows you to selectively replace some of its
# fields:

my_car._replace(color='blue')
print(my_car)

# _make() classmethod can be used to create new instances
# of a namedtuple from a sequence or iterable:
new = Car._make(['red', 999])
print(new)



