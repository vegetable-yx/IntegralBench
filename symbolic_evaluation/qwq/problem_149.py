import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Compute the final result by dividing π² by √2
result = pi_squared / sqrt_two

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))