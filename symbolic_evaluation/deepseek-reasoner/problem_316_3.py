import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate the denominator: 4 * sqrt(2)
denominator = 4 * mp.sqrt(2)

# Compute the final result by dividing π² by the denominator
result = pi_squared / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))