import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt_2

# Multiply by -3 to get final result
result = -3 * pi_times_sqrt2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))