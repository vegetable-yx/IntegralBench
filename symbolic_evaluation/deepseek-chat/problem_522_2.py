import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Calculate the denominator: square root of 2019
denominator = mp.sqrt(2019)

# Compute the final result: sqrt(pi) / sqrt(2019)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))