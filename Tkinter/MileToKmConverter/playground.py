def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum


print(add(2, 3, 4))

def calculate(n, **kwargs):
    print(kwargs)
    print (kwargs["add"])
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get["make"]
        self.model = kwargs.get["model"]
        self.colour = kwargs.get["colour"]
        self.seats = kwargs.get["seats"]
my_car = Car(seats=5)
print(my_car.seats)