import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Add 1 to the square root of 2
one_plus_sqrt2 = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(one_plus_sqrt2)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))