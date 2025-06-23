import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Define numerator and denominator using arbitrary precision
numerator = mp.mpf(5)
denominator = mp.mpf(6)

# Perform exact fraction division
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))