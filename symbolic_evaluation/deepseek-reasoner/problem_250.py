import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate (sqrt(2) - 1)
sqrt_term = sqrt_2 - 1

# Multiply by pi to get final result
result = mp.pi * sqrt_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))