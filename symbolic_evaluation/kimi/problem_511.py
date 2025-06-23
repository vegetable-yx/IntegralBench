import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 8
sqrt_8 = mp.sqrt(8)

# Calculate sine of the square root value
sin_sqrt8 = mp.sin(sqrt_8)

# Multiply by 2 to get final result
result = 2 * sin_sqrt8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))