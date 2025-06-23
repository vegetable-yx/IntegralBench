import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate the rational number component
rational_part = mp.mpf(10747) / 10

# Calculate the logarithmic component
logarithmic_part = 6 * mp.log(2)

# Combine components for final result
result = rational_part + logarithmic_part

# Print with 10 decimal precision
print(mp.nstr(result, n=10))