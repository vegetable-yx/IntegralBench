import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π/2
pi_half = mp.pi / 2

# Compute natural logarithm of π/2
result = mp.log(pi_half)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))