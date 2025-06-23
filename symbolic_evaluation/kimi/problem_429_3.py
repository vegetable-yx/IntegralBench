import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 4*ln(2) component
ln2 = mp.log(2)
term1 = 4 * ln2

# Calculate ln(23/5) component
fraction = mp.mpf(23)/5  # Convert to precise floating-point
term2 = mp.log(fraction)

# Combine components for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))