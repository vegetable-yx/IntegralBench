import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 4 * natural logarithm of 2
ln2 = mp.log(2)
term1 = 4 * ln2

# Calculate natural logarithm of (5/23)
fraction = mp.mpf(5)/23  # Create precise fraction 5/23
term2 = mp.log(fraction)

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))