import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to the fourth power
pi4 = mp.pi ** 4

# Multiply by 2
numerator = 2 * pi4

# Divide by 315 and apply the negative sign
result = -numerator / 315

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))