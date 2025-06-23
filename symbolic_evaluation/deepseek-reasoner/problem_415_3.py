import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator and denominator using exact mpmath types
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Perform exact division operation
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))