import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply pi by sqrt(2)
pi_times_sqrt_two = mp.pi * sqrt_two

# Divide by 4 to get the final result
result = pi_times_sqrt_two / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))