import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 4 to get the result
result = pi_squared / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))