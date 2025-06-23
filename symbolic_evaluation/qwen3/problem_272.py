import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate components of the expression
sqrt2 = mp.sqrt(2)                # Compute √2
log_numerator = 1 + sqrt2         # Calculate numerator of log argument
log_arg = log_numerator / 2       # Compute (1+√2)/2 for logarithm
log_term = mp.log(log_arg)        # Calculate natural logarithm term

# Combine components according to the formula
combined_terms = sqrt2 - 1 - log_term  # Combine √2 - 1 - ln(...)
result = (mp.pi / 2) * combined_terms  # Multiply by π/2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))