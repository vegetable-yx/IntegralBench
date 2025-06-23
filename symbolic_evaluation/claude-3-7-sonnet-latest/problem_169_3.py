import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_value = mp.pi
pi_squared = pi_value ** 2

# Print the result to 10 decimal places
print(mp.nstr(pi_squared, n=10))