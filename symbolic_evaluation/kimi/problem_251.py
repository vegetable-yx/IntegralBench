import mpmath as mp
mp.dps = 15

# Calculate 1 + sqrt(2)
sqrt_val = mp.sqrt(2)
sum_term = 1 + sqrt_val

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(sum_term)

# Multiply by pi to get final result
result = mp.pi * log_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))