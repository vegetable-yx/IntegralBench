import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Add 1 to the square root of 2
one_plus_sqrt2 = 1 + sqrt2

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Multiply by pi to get the final result
result = mp.pi * log_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))