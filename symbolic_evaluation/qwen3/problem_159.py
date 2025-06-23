import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate hyperbolic sine of 4
sinh_val = mp.sinh(4)

# Multiply by 4 to get the final result
result = 4 * sinh_val

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))