import numfuns as nf
from numfuns import nexteven, SIZE
from math import *
import math
import sys

print(sys.path)  # Module Search Path
# Modify search path by adding new folder
sys.path.insert(0, r'c:\classroom\python\demo\lib')

import strfuns as sf
print(sf.startswithupper('Hello'))

print(nf.iseven(10), nf.nexteven(23))
print(nexteven(10), SIZE, pi)

# print(dir(nf))
# print(dir(math))
