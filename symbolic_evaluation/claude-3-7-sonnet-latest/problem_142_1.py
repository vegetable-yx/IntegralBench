import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute pi/4 using mpmath constants
pi_over_4 = mp.pi / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(pi_over_4, n=10))