import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
sum_value = 1 + sqrt2

# Calculate natural logarithm of the sum
log_term = mp.log(sum_value)

# Multiply by pi to get final result
result = mp.pi * log_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))