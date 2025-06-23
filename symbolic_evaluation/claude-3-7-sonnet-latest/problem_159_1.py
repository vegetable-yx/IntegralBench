import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sinh(4) - hyperbolic sine of 4
sinh_val = mp.sinh(4)

# Multiply by 4 to get final result
result = 4 * sinh_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))