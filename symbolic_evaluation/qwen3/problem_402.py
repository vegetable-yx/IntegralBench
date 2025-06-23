import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate π/3
pi_over_3 = mp.pi / 3

# Compute natural logarithm of π/3
log_pi_over_3 = mp.log(pi_over_3)

# Multiply by 2 to get final result
result = 2 * log_pi_over_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))