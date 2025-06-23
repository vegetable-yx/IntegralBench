import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(1 + sqrt_2)

# Square the logarithmic term
log_squared = log_term ** 2

# Multiply by pi/8 to get final result
result = (mp.pi / 8) * log_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))