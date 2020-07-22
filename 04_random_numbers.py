# Component four (1) - generating random numbers
# Random numbers will be used in place of 'x' and 'y' in (x + y = z) where z is user answer input

import random

# List of ten items
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Prints 10 items (from list statement) in range (1, 100) with 2 decimal points

for a, b in enumerate(list, 1):

    print("#{} = {:.2f}".format(a, round(random.uniform(1, 100), 2)))

