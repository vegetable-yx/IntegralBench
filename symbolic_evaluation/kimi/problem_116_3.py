import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))