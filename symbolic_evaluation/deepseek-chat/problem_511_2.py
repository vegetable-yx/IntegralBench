import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply the square root by 2
two_sqrt2 = 2 * sqrt2

# Compute the sine of (2 * sqrt(2))
sin_val = mp.sin(two_sqrt2)

# Multiply the sine value by 2 to get the result
result = 2 * sin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))