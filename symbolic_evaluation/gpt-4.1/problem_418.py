import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π squared by 6
term = pi_squared / 6

# Subtract 1 to get the final result
result = term - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))