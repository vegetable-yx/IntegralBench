import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Square the logarithmic term
log_squared = log_term ** 2

# Multiply by pi/4 to get final result
result = (mp.pi / 4) * log_squared

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))