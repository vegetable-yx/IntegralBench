import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate the denominator 2*sqrt(2)
denominator = 2 * mp.sqrt(2)

# Compute the final result by dividing π² by the denominator
result = pi_squared / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))