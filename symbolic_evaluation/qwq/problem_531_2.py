import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using exact fractions
numerator = mp.mpf(5)
denominator = mp.mpf(6)

# Perform exact division with mpmath precision
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))