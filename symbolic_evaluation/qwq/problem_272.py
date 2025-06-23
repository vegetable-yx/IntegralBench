import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each component of the expression step by step
sqrt2 = mp.sqrt(2)  # Calculate square root of 2
log_argument = (sqrt2 + 1) / 2  # Compute argument for the logarithm
log_term = mp.log(log_argument)  # Calculate natural logarithm term

# Combine components according to the formula
combined_terms = sqrt2 - 1 - log_term  # Combine sqrt(2) - 1 - ln(...)
result = (mp.pi / 2) * combined_terms  # Multiply by π/2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))