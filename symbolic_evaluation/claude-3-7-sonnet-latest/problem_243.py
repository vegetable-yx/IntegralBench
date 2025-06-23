import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide by 8 to get the result
result = pi_squared / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))