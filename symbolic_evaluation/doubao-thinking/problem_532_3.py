import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(pi_squared, n=10))