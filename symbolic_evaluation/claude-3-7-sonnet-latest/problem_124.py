import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 16 to get the result
result = pi_squared / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))