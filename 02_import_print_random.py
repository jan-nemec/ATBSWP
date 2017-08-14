# An import statement consists of the following:
# The import keyword
# The name of the module
# Optionally, more module names, as long as they are separated by commas

import random  # import random, sys, os, math
# from random import randint
# from random import *

for i in range(5):
    print(random.randint(1, 10))
# Since randint() is in the random module, you must first type random.
# in front of the function name to tell Python to look for this function inside the random module.
