import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 8 * π using mpmath's pi constant
denominator = mp.mpf(8) * mp.pi

# Compute the reciprocal of (8π)
result = mp.mpf(1) / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))