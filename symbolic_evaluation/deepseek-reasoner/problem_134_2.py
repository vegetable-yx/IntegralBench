import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Get pi constant
pi_value = mp.pi

# Multiply the components to get final result
result = sqrt_2 * pi_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))