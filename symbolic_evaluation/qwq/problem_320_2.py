import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator using exact values
numerator = mp.mpf(3)
denominator = mp.mpf(2)

# Compute the exact fraction
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))