import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate components step by step
sqrt2 = mp.sqrt(2)  # Compute √2
log_argument = (1 + sqrt2) / 2  # Calculate (1 + √2)/2 for logarithm
log_term = mp.log(log_argument)  # Compute natural logarithm of the argument
combined_terms = sqrt2 - 1 - log_term  # Combine all components inside parentheses
result = (mp.pi / 2) * combined_terms  # Multiply by π/2

print(mp.nstr(result, n=10))