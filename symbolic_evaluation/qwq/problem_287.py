import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Square the logarithmic term
log_squared = log_term ** 2

# Multiply by pi and divide by 8
result = (mp.pi / 8) * log_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))