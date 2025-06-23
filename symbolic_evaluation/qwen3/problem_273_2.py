import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component of the expression step by step
sqrt2 = mp.sqrt(2)  # Compute sqrt(2)

# Compute the argument for the logarithm
log_arg = (sqrt2 + 1) / 2

# Calculate the natural logarithm term
log_term = mp.log(log_arg)

# Compute each part of the main expression
term1 = 4 * sqrt2
term2 = -5
term3 = 12 * log_term

# Combine all terms and multiply by pi/72
sum_terms = term1 + term2 + term3
result = (mp.pi / 72) * sum_terms

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))