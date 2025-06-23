import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate first term: -1/16 * sin(2)
sin_term = mp.sin(2)
term1 = (-mp.mpf(1)/16) * sin_term

# Calculate second term: -3/8 * cos(2)
cos_term = mp.cos(2)
term2 = (-mp.mpf(3)/8) * cos_term

# Combine terms for final result
result = term1 + term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))