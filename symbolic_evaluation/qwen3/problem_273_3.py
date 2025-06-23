import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt2 = mp.sqrt(2)  # Compute square root of 2
log_arg = (3 + 2*sqrt2)/4  # Calculate argument for logarithm
log_term = mp.log(log_arg)  # Compute natural logarithm

# Combine all terms in the numerator
linear_terms = 4*sqrt2 - 5
combined_terms = linear_terms + 6*log_term

# Multiply by π and divide by 72 for final result
result = (mp.pi / 72) * combined_terms

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))