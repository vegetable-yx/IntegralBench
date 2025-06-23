import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi
pi_term = mp.pi * sqrt_2

# Multiply by coefficient -3
result = -3 * pi_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))