import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Compute the square of pi: π^2
pi_squared = mp.pi ** 2

# Print the result formatted to 10 decimal places
print(mp.nstr(pi_squared, n=10))