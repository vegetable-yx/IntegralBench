import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate numerator and denominator
numerator = mp.mpf(20)
denominator = mp.mpf(3)

# Compute the exact fraction
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))