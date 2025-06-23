import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator using exact integer values
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Perform exact fraction division
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))