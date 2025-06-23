import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = 2
denominator = mp.pi

# Compute the final result
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))