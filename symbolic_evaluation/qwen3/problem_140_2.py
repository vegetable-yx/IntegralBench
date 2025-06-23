import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e squared
e_squared = mp.exp(2)

# Compute each term separately
term1 = 13 * e_squared
term2 = 19 / e_squared
term3 = -28

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))