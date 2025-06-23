import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Multiply by pi to get final result
result = mp.pi * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))