# Erbol Zamirov
# May 16, 2025

# Problem 6: Calculate the factorial of a user input value using a for loop.
# Also print the factorial calculated using math.factorial.

import math

n = int(input("Enter a non-negative integer: "))

factorial_manual = 1
for i in range(1, n + 1):
    factorial_manual *= i

factorial_math = math.factorial(n)

print(f"Factorial (manual calculation): {factorial_manual}")
print(f"Factorial (math.factorial function): {factorial_math}")