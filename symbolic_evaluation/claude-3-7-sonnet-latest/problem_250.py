import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate pi/2 using mpmath's constant for pi
pi_over_2 = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(pi_over_2, n=10))