import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the components of the expression step by step
sqrt2 = mp.sqrt(2)                # Compute square root of 2
log_arg = 1 + sqrt2               # Argument for logarithm function
log_term = mp.log(log_arg)        # Compute natural logarithm of (1 + sqrt(2))
log_squared = log_term ** 2       # Square the logarithmic term
pi_over_8 = mp.pi / 8             # Compute π/8 coefficient
result = pi_over_8 * log_squared  # Combine components for final result

print(mp.nstr(result, n=10))      # Print result with 10 decimal places