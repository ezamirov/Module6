# Erbol Zamirov
# May 16, 2025


# Problem 4: Approximate pi using a simple arithmetic method and print the approximation
# and the value of math.pi from the math module.

import math

# One simple approximation for pi is the Leibniz formula:
# pi ≈ 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... )
# We'll compute the sum of the first N terms.

N = 10000  # number of terms in the series
approx_pi = 0
for i in range(N):
    term = ((-1) ** i) / (2 * i + 1)
    approx_pi += term

approx_pi *= 4

print("Approximation of pi:", approx_pi)
print("Value of math.pi:", math.pi)
