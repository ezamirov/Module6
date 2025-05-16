# Erbol Zamirov
# May 16, 2025

# Problem 5: Convert radians to degrees given a user input value.
# Print the converted value and also the value using math.degrees function.

import math

radians = float(input("Enter angle in radians: "))

# Conversion formula: degrees = radians * (180/pi)
degrees_manual = radians * (180 / math.pi)

degrees_math = math.degrees(radians)

print(f"Degrees (manual calculation): {degrees_manual}")
print(f"Degrees (math.degrees function): {degrees_math}")