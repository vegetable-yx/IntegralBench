import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/4 directly using mpmath's constant for pi
pi_over_4 = mp.pi / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(pi_over_4, n=10))