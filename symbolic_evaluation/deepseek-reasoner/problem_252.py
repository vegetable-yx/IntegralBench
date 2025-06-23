import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 1 + sqrt(2)
sqrt_part = mp.sqrt(2) + 1

# Compute natural logarithm of (1 + sqrt(2))
log_part = mp.log(sqrt_part)

# Multiply by pi to get final result
result = mp.pi * log_part

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))