import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 1 + sqrt(2)
sqrt2 = mp.sqrt(2)
base = 1 + sqrt2

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(base)

# Square the logarithmic term
log_squared = log_term ** 2

# Multiply by pi/8 to get final result
result = (mp.pi / 8) * log_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))