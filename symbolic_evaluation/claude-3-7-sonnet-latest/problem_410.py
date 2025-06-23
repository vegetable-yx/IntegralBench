import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate the numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Calculate the denominator: 2 times Euler's number
denominator = 2 * mp.e

# Compute the result: sqrt(pi) / (2e)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))