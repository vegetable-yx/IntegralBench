import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute π using mpmath's constant
pi_val = mp.pi

# Square π to get π²
pi_squared = pi_val ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(pi_squared, n=10))