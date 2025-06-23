import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the numerator (3 * π)
numerator = mp.mpf(3) * mp.pi

# Calculate the denominator (16)
denominator = mp.mpf(16)

# Compute the final result by dividing numerator by denominator
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))