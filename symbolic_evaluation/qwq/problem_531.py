import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator and denominator
numerator = mp.mpf(5)
denominator = mp.mpf(6)

# Compute the exact fraction
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))