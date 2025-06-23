import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components separately
sqrt2 = mp.sqrt(2)  # Compute √2
ln2 = mp.log(2)     # Compute natural logarithm of 2

# Combine components according to the expression -4√2πln2
result = -4 * sqrt2 * mp.pi * ln2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))