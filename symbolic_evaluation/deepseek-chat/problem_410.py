import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Compute denominator: 2 times Euler's number e
denominator = 2 * mp.e

# Calculate the result: sqrt(pi) / (2e)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))