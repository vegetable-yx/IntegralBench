import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 1 + sqrt(2)
sqrt2 = mp.sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Multiply by pi to get the final result
result = mp.pi * log_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))