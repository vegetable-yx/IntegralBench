import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: 1 + sqrt(2)
log_arg = 1 + sqrt2

# Calculate the natural logarithm of (1 + sqrt(2))
log_val = mp.log(log_arg)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))