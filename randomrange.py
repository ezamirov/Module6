# Erbol Zamirov
# May 16, 2025

# Problem 1: Use a for statement and random.randrange to print 10 random integers between 25 and 35.

import random

for _ in range(10):
    # random.randrange(start, stop) generates a random integer from start up to stop-1
    num = random.randrange(25, 36)  # 36 because stop is exclusive, to include 35
    print(num)