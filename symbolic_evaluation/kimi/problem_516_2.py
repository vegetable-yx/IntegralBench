import mpmath as mp

# Set internal decimal precision to 15 digits for accurate calculations
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Subtract 1 from π/2
result = pi_over_2 - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))