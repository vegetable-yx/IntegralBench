import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Multiply by pi
pi_times_sqrt3 = mp.pi * sqrt3

# Divide by 3 to get the final result
result = pi_times_sqrt3 / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))