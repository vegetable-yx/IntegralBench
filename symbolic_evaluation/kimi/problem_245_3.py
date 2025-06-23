import mpmath as mp
mp.dps = 15  # Set decimal precision

# Calculate numerator and denominator using arbitrary precision
numerator = mp.mpf(3)
denominator = mp.mpf(32)

# Perform exact fraction division
result = numerator / denominator

# Print result with 10 decimal place formatting
print(mp.nstr(result, n=10))