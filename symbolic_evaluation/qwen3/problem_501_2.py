import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using exact fractions
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform exact division
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))