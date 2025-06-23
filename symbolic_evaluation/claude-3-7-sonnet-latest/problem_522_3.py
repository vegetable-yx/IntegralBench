import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Calculate the denominator: square root of 2019
denominator = mp.sqrt(2019)

# Compute the result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))