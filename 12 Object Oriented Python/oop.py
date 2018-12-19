"""
DEFINITIONS

class: template for creating objects
object: an instance of a class
instantiate: create an instance of a class
method: a function defined in a class
attribute: a variable bound to an instance of a class

"""
class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.33)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood,hamilton))

print(kenwood.on)

hamilton.switch_on()

print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

# one can generate an attribute
kenwood.power = 1.5
print(kenwood.power)
