import mpmath as mp

# Set the decimal precision for calculations
mp.dps = 15

# Compute pi raised to the 4th power
pi_4 = mp.pi ** 4

# Multiply the result by 3
numerator = 3 * pi_4

# Divide by 8 to get the final result
result = numerator / 8

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))