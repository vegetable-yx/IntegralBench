import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2 using mpmath's pi constant
pi_over_2 = mp.pi / 2

# Compute natural logarithm of π/2 using mpmath's log function
log_term = mp.log(pi_over_2)

# Multiply by 1/2 to get the final result
result = 0.5 * log_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))