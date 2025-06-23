import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate numerator: 3 * pi
numerator = mp.mpf(3) * mp.pi

# Calculate denominator: 32
denominator = mp.mpf(32)

# Compute the result: (3 * pi) / 32
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))