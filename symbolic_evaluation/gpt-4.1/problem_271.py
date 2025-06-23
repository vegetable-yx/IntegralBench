import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 17 * pi
numerator = mp.mpf(17) * mp.pi

# Calculate the denominator
denominator = mp.mpf(256)

# Compute the result: (17 * pi) / 256
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))