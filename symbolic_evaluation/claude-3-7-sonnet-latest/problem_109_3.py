import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt_two = mp.pi * sqrt_two

# Divide by 2 to get the final result
result = pi_times_sqrt_two / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))