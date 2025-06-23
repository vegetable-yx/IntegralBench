import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π divided by 3
pi_over_3 = mp.pi / 3

# Compute natural logarithm of the ratio
log_result = mp.log(pi_over_3)

# Multiply by 2 for final result
result = 2 * log_result

# Print with 10 decimal precision
print(mp.nstr(result, n=10))