import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute π/4 using mpmath's constant pi
pi_over_4 = mp.pi / 4

# Format the result to exactly 10 decimal places and print
print(mp.nstr(pi_over_4, n=10))