import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π squared
pi_squared = mp.pi ** 2

# Print result to exactly 10 decimal places
print(mp.nstr(pi_squared, n=10))