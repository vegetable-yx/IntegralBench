import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the rational number term
rational_term = mp.mpf(10747)/10

# Calculate the logarithmic term with coefficient
log_term = 6 * mp.log(2)

# Combine both terms for final result
result = rational_term + log_term

# Print with 10 decimal precision
print(mp.nstr(result, n=10))