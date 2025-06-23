import mpmath as mp
mp.dps = 15  # Set decimal precision

# Calculate simple fraction components
numerator = mp.mpf(1)
denominator = mp.mpf(2)

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))