import math
import sys   # import <module>
import math,sys   # We can do like this also.
print(math.pi)   # Using math module to print pi variable.

from math import pi,e   # We import some concretical variables.
print(pi)
print(e)

from math import *   # We can like this eighter but it isn`t very secure.

import math as m   # We import math with the name m.
print(m.pi)

from math import pi as PI, sin as sine   # We can var names in module too.
print(PI)
print(sine)

dir(math)   # All available variables and methods if they exits.

import random   # Random!

for i in range(5):
    print(random.random())

random.seed(0)
random.seed(10)

my_list = [i for i in range(11)]

print(random.choice(my_list))
print(random.sample(my_list,5))

import platform as p   # Module to see sys info.
print(p.platform())   # Your platform.
print(p.platform(1))
print(p.platform(0,1))

print(p.machine())   # Your pc info.

print(p.system())   # Your OS info.

print(p.version())   # Version of your OS.

