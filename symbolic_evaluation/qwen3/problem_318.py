import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate denominator 3π
denominator = mp.mpf(3) * mp.pi

# Compute the final result 4/(3π)
result = mp.mpf(4) / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))