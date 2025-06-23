import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator as exact fractions
numerator = mp.mpf(47)
denominator = mp.mpf(60)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))