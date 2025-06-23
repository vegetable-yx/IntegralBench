import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the components of the expression step by step
sqrt2 = mp.sqrt(2)  # Compute √2
log_argument = 1 + sqrt2  # Calculate (1 + √2)
ln_value = mp.log(log_argument)  # Compute ln(1 + √2)
ln_squared = ln_value ** 2  # Square the logarithm value
pi_over_8 = mp.pi / 8  # Calculate π/8

# Combine components for final result
result = pi_over_8 * ln_squared

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))