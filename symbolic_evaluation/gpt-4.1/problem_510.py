import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute numerator: 7 * pi
numerator = mp.mpf(7) * mp.pi

# Compute denominator: 3 * sqrt(3)
denominator = mp.mpf(3) * mp.sqrt(3)

# Compute the final result: (7 * pi) / (3 * sqrt(3))
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))