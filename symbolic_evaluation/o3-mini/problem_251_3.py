import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(one_plus_sqrt2)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))