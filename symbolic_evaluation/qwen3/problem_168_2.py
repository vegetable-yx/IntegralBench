import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 2 to get the final result
result = 2 * pi_squared

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))