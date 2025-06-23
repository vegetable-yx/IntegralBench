import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by coefficient 8
eight_sqrt2 = 8 * sqrt2

# Multiply by pi to get final result
result = eight_sqrt2 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))