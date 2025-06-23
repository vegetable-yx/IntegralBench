import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 2 to get the result
result = pi_squared / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))