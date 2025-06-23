import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate sine and cosine of 1 radian
sin_val = mp.sin(1)
cos_val = mp.cos(1)

# Compute each term with its coefficient
term1 = 8 * sin_val
term2 = 4 * cos_val
term3 = -8

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal places
print(mp.nstr(result, n=10))