import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate numerator: 7 * π
numerator = mp.mpf(7) * mp.pi

# Calculate denominator: 3 * sqrt(3)
sqrt3 = mp.sqrt(3)
denominator = mp.mpf(3) * sqrt3

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))