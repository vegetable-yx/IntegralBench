import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by coefficient 5
five_sqrt2 = 5 * sqrt2

# Multiply by pi
numerator = five_sqrt2 * mp.pi

# Divide by 8 to get final result
result = numerator / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))