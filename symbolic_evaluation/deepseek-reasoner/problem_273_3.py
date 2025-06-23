import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each term of the expression separately
term1 = 3 * mp.pi / 8

term2 = -mp.pi * mp.sqrt(2) / 18

term3 = -mp.mpf(5)/27  # Exact rational number conversion

# Calculate logarithmic term components
log_arg = (1 + mp.sqrt(2)) / 2
log_term = mp.log(log_arg)
term4 = -(mp.pi / 6) * log_term

# Combine all terms
result = term1 + term2 + term3 + term4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))