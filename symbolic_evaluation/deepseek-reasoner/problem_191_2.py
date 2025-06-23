import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_squared = mp.pi ** 2

# Multiply by 3 to get the numerator
numerator = 3 * pi_squared

# Divide by 512 to get the final result
result = numerator / 512

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))