# Component four, generate two random 2dp values in a range for quiz question

import random

# List of ten items
long_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Prints the preceding list and adds a random 2dp number between 1 and 100 to each item on list
# 1 and 100 are the value im going with for my addition game, might change later
for a, b in enumerate(long_list, 1):
    print("#{} = {:.2f}".format(a, round(random.uniform(1, 100), 2)))

