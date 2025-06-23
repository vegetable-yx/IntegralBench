import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π/2
pi_over_2 = mp.pi / 2

# Calculate result: π/2 - 1
result = pi_over_2 - 1

# Print result to 10 decimal places
print(mp.nstr(result, n=10))