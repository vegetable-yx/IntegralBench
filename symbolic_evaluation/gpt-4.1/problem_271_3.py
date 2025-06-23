import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator: 19 * pi
numerator = mp.mpf(19) * mp.pi

# Define denominator
denominator = mp.mpf(512)

# Compute the result: (19 * pi) / 512
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))