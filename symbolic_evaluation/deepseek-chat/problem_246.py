import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi to the fourth power
pi4 = mp.pi**4

# Multiply by 135
numerator = 135 * pi4

# Divide by 8
result = numerator / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))