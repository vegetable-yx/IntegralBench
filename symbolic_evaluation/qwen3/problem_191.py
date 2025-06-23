import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide by 128 to get the final result
result = pi_squared / 128

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))