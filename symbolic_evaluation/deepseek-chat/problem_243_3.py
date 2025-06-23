import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate pi to the fourth power
pi4 = mp.pi**4

# Multiply by 7 to get the numerator
numerator = 7 * pi4

# Divide by 2160 to get the final result
result = numerator / 2160

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))