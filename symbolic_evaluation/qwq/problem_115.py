import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate components separately
sqrt2 = mp.sqrt(2)  # Compute square root of 2
log_argument = 1 + sqrt2  # Calculate argument for logarithm
log_term = mp.log(log_argument)  # Compute natural logarithm
pi_quarter = mp.pi / 4  # Calculate π/4

# Multiply components to get final result
result = pi_quarter * log_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))