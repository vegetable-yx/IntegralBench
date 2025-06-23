import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 2
two_sqrt_2 = 2 * sqrt_2

# Multiply by pi to get final result
result = two_sqrt_2 * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))