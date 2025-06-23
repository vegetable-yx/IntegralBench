import mpmath as mp
mp.dps = 15

# Calculate numerator: 5 * π
numerator = 5 * mp.pi

# Calculate denominator: 4 * sqrt(2)
denominator = 4 * mp.sqrt(2)

# Compute the final result
result = numerator / denominator

print(mp.nstr(result, n=10))