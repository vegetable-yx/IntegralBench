import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Multiply by coefficient 7
seven_sqrt3 = 7 * sqrt3

# Multiply by pi
pi_times_term = mp.pi * seven_sqrt3

# Divide by 9 to get final result
result = pi_times_term / 9

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))