import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate the rational number component
rational_part = mp.mpf(10747) / 10

# Calculate the logarithmic component
log_term = mp.log(2)  # Natural logarithm of 2
log_part = 6 * log_term

# Combine components for final result
result = rational_part + log_part

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))