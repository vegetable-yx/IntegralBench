import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Perform exact division
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))