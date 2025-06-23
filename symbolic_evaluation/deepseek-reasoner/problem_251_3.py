import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
sum_term = 1 + sqrt2

# Calculate natural logarithm of the sum
log_term = mp.log(sum_term)

# Multiply by pi to get final result
result = mp.pi * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))