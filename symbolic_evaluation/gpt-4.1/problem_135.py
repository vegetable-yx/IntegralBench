import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 3 * pi
numerator = mp.mpf(3) * mp.pi

# Calculate the denominator
denominator = mp.mpf(4)

# Compute the result: (3 * pi) / 4
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))