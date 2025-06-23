import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Calculate the denominator: square root of 2019
denominator = mp.sqrt(2019)

# Compute the final result by division
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))