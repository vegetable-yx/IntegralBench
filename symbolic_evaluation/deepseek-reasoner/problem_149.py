import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Compute final result by dividing π² by √2
result = pi_squared / sqrt_two

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))