import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute natural logarithm of π/2
result = mp.log(pi_over_2)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))