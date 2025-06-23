import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 4 to get the final result
result = pi_squared / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))