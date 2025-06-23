import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the numerator: 19 * π
numerator = mp.mpf(19) * mp.pi

# Compute the denominator
denominator = mp.mpf(512)

# Final result: (19 * π) / 512
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))