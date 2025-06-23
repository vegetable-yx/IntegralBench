import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression step by step
sqrt5 = mp.sqrt(5)          # Compute square root of 5
log_argument = 2 + sqrt5    # Calculate argument for logarithm
log_term = mp.log(log_argument)  # Compute natural logarithm
pi_over_4 = mp.pi / 4       # Calculate π/4

# Combine components for final result
result = pi_over_4 * log_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))