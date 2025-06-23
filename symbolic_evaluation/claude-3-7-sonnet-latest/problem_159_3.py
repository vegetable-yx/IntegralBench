import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sinh(4)
sinh_val = mp.sinh(4)

# Multiply by 8 to get final result
result = 8 * sinh_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))