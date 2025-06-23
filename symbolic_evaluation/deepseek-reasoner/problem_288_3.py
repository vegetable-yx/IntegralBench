import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate first term: π³ divided by 48
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 48

# Calculate components for the second term
sqrt2 = mp.sqrt(2)                # Compute √2
log_argument = 1 + sqrt2          # Argument for logarithm
log_value = mp.log(log_argument)  # Compute ln(1 + √2)
log_squared = log_value ** 2      # Square the logarithm result

# Calculate second term: π multiplied by squared log divided by 4
term2 = (mp.pi * log_squared) / 4

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))