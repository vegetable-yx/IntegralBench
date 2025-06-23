import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi to the fourth power
pi4 = mp.pi ** 4

# Multiply by 7
numerator = 7 * pi4

# Divide by 16 to get the final result
result = numerator / 16

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))