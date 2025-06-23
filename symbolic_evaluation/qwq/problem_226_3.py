import mpmath as mp
mp.dps = 15

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Square the logarithm term
log_squared = log_term ** 2

# Compute pi squared
pi_squared = mp.pi ** 2

# Multiply pi squared with squared logarithm
numerator = pi_squared * log_squared

# Final result after division by 4
result = numerator / 4

print(mp.nstr(result, n=10))