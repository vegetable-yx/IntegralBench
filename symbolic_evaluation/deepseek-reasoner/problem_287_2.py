import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate first term: π³ divided by 192
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 192

# Calculate components for second term
sqrt2 = mp.sqrt(2)          # Compute √2
log_argument = 1 + sqrt2    # Calculate 1+√2
log_value = mp.log(log_argument)  # Compute ln(1+√2)
log_squared = log_value ** 2      # Square the logarithm
term2 = (mp.pi * log_squared) / 8  # Combine with π and denominator

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))