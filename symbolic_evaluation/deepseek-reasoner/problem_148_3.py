import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate denominator (4 * sqrt(2))
denominator = 4 * sqrt_2

# Compute final result by dividing π² by the denominator
result = pi_squared / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))