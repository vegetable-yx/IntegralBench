import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Compute the constant pi
pi_value = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(pi_value, n=10))