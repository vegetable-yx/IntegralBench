import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Calculate numerator for logarithm argument
log_numerator = sqrt2 + 1

# Compute the logarithm argument
log_arg = log_numerator / 2

# Calculate natural logarithm term
log_term = mp.log(log_arg)

# Combine all components inside the parentheses
sum_terms = sqrt2 - 1 + log_term

# Multiply by pi/2 for final result
result = (mp.pi / 2) * sum_terms

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))