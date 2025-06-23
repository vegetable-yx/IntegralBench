import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/2 directly using mpmath's constant
pi_half = mp.pi / 2

# Print result with 10 decimal places precision
print(mp.nstr(pi_half, n=10))