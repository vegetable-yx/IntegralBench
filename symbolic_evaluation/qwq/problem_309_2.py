import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate components separately
sqrt2 = mp.sqrt(2)  # Compute square root of 2
log_argument = 1 + sqrt2  # Compute argument for logarithm
log_term = mp.log(log_argument)  # Calculate natural logarithm
pi_times_log = mp.pi * log_term  # Multiply by pi

# Final calculation combining components
result = pi_times_log / sqrt2  # Divide by sqrt(2)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))