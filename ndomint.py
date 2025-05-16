# Erbol Zamirov
# May 16, 2025

# Problem 2: Use random.randrange to print an odd integer between 0 and 100.

import random

# random.randrange(start, stop, step) can be used to generate odd numbers only by stepping by 2 from 1
odd_num = random.randrange(1, 100, 2)  # odd integers between 1 and 99
print(odd_num)