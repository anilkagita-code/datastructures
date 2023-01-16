# -*- coding: utf-8 -*-
"""


@author: anil_
"""


class Kettle(object):
    power_source = 'Electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        if self.on == False:
            self.on = True
        else:
            self.on = False


kenwood = Kettle("Kenwood", 10)
print(kenwood.make, kenwood.price)

kenwood.price = 12.10

print(kenwood.make, kenwood.price)

hamilton = Kettle('Hamilton', 15.25)

print(f'Models: {kenwood.make} {kenwood.price}')

print(f'{hamilton.on}')
hamilton.switch_on()
print(f'{hamilton.on}')

Kettle.switch_on(hamilton)
print(f'{hamilton.on}')

print('\nSetting up variable only for one instance of a class and checking other instances')
kenwood.power = 1.5
print(kenwood.power)

print(
    '\nprint(hamilton.power) shall through an error since its only set for kenwood not for hamilton and also not for the Kettle Class')

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print('\nSetting up variable only for one instance of a class and checking other instances')

print(Kettle.power_source, kenwood.power_source, hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print('\nChanging the power source')
kenwood.power_source = 'Wind'
Kettle.power_source = 'Atomic'
print(Kettle.power_source, kenwood.power_source, hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
