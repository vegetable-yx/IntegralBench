import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi constant
pi_times_sqrt2 = mp.pi * sqrt_2

# Multiply by 2 to get the final result
result = 2 * pi_times_sqrt2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))