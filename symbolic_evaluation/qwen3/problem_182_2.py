import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt5 = mp.sqrt(5)  # Compute square root of 5
log_argument = 2 + sqrt5  # Compute argument for logarithm
log_term = mp.log(log_argument)  # Compute natural logarithm term
fraction_term = (1 - sqrt5) / 2  # Compute (1 - sqrt(5))/2 term

# Combine all components
combined_terms = log_term + fraction_term
result = mp.pi * combined_terms  # Multiply by pi

print(mp.nstr(result, n=10))  # Print result with 10 decimal places