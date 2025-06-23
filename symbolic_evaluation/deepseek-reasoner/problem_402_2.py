import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π divided by 3
pi_over_3 = mp.pi / 3

# Compute the natural logarithm of π/3 using mp.log
log_pi_over_3 = mp.log(pi_over_3)

# Multiply the logarithm result by 2
result = 2 * log_pi_over_3

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))