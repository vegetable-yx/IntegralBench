import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 8 to get the result
result = pi_squared / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))