import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Calculate the logarithmic term argument
log_arg = 2 + sqrt5

# Compute natural logarithm of (2 + sqrt(5))
log_term = mp.log(log_arg)

# Combine all components of the expression
term1 = 1 - sqrt5
term2 = 2 * log_term
combined_terms = term1 + term2

# Multiply by pi/2 for final result
result = (mp.pi / 2) * combined_terms

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))