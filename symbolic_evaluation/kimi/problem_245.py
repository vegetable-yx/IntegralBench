import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator as exact fractions
numerator = mp.mpf(45)
denominator = mp.mpf(64)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))