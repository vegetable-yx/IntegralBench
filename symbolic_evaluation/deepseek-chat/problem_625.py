import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply by pi
pi_times_sqrt2 = mp.pi * sqrt_two

# Divide by 4 to get the final result
result = pi_times_sqrt2 / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))