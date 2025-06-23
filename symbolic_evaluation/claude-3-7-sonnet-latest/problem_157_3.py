import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 8 * sqrt(pi)
numerator = 8 * mp.sqrt(mp.pi)

# Calculate the denominator: exp(1/4)
denominator = mp.exp(1/4)

# Compute the final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))