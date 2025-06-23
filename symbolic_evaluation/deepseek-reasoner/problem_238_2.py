import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator and denominator
numerator = mp.mpf(20)
denominator = mp.mpf(3)

# Perform exact division
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))