import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 1 + sqrt(2)
sqrt2 = mp.sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(one_plus_sqrt2)

# Square the logarithmic term
log_squared = log_term ** 2

# Multiply by pi and divide by 8
result = (mp.pi * log_squared) / 8

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))