import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 8 to obtain the result
result = pi_squared / 8

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))