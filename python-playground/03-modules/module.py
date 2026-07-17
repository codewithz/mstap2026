
# ----------------------------------------------------------------------
# The Python Standard Library
# ----------------------------------------------------------------------
# Python ships with a large collection of ready-to-use modules -- this is
# often called "batteries included". A module is just a .py file full of
# reusable code (functions, classes, variables) that someone else already wrote.

import math
print(type(math))
# Output:
# <class 'module'>

# ----------------------------------------------------------------------
# Importing an entire module
# ----------------------------------------------------------------------
import math
print(math.pi)
print(math.sqrt(16))
# Output:
# 3.141592653589793
# 4.0

# ----------------------------------------------------------------------
# Importing specific names from a module
# ----------------------------------------------------------------------
from math import pi, sqrt
print(pi)
print(sqrt(25))
# Output:
# 3.141592653589793
# 5.0

# ----------------------------------------------------------------------
# Aliasing an import (giving it a shorter/different name)
# ----------------------------------------------------------------------
import math as m
print(m.pi)

from math import sqrt as square_root
print(square_root(36))
# Output:
# 3.141592653589793
# 6.0

# ----------------------------------------------------------------------
# Importing everything from a module (use sparingly!)
# ----------------------------------------------------------------------
from math import *
print(floor(4.7))
print(ceil(4.2))
# Output:
# 4
# 5

# ----------------------------------------------------------------------
# Listing the names available inside a module
# ----------------------------------------------------------------------
import math
print(dir(math))
# Output:
# ['__doc__', '__loader__', '__name__', ... 'pi', 'pow', ... 'sqrt', ...]
# (full list -- run it yourself to see every name math provides)

# ----------------------------------------------------------------------
# Where do modules come from? Three sources:
# 1. Built-in modules that ship with Python (math, os, sys, json, random...)
# 2. Third-party packages you install with pip (requests, numpy, pandas...)
# 3. Your own .py files -- any script you write can be imported by another script
# ----------------------------------------------------------------------

import random
print(random.randint(1, 10))
# Output:
# (a random whole number between 1 and 10 -- will differ every run)

import os
print(os.getcwd())
# Output:
# (your current working folder -- will differ on your machine)

# ----------------------------------------------------------------------
# A note on packages
# ----------------------------------------------------------------------
# A "package" is just a folder of related modules, grouped together, e.g.:
#
#   utils/
#     __init__.py
#     constants/
#       metric.py
#     messages/
#       french.py
#
# You'd import from it the same way: from utils.constants import metric
# Third-party packages installed with "pip install <name>" work identically --
# pip just downloads the package's files into your (virtual) environment so
# "import" can find them.
# Output:
# Cart sorted by price, highest first: [('Bread', 15, 2), ('Butter', 7, 3), ('Jam', 3, 1)]