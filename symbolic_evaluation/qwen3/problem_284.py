import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 1 + sqrt(2)
sqrt2 = mp.sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Compute natural logarithm of (1 + sqrt(2))
ln_term = mp.log(one_plus_sqrt2)

# Square the logarithmic term
ln_squared = ln_term ** 2

# Calculate pi/8
pi_over_8 = mp.pi / 8

# Combine components for final result
result = pi_over_8 * ln_squared

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))