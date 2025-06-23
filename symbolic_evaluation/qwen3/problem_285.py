import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt2 = mp.sqrt(2)
log_arg = 1 + sqrt2
log_term = mp.log(log_arg)
log_squared = log_term ** 2

# Compute each term of the main expression
term1 = (mp.pi / 8) * log_squared
term2 = -sqrt2 / 2
term3 = mp.mpf(1)/2  # Exact 0.5 representation

# Combine all terms for final result
result = term1 + term2 + term3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))