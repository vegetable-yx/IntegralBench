import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Compute final result by dividing pi squared by sqrt(2)
result = pi_squared / sqrt_2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))