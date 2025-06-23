import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute sqrt(2) using mpmath's square root function
sqrt_2 = mp.sqrt(2)

# Calculate 1 + sqrt(2)
sum_value = 1 + sqrt_2

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(sum_value)

# Multiply by pi to get final result
result = mp.pi * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))