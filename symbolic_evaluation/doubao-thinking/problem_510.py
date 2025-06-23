import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Multiply by the square root of 3
pi_times_sqrt3 = mp.pi * sqrt3

# Multiply by 7 to get the numerator
numerator = 7 * pi_times_sqrt3

# Divide by 9 to get the final result
result = numerator / 9

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))