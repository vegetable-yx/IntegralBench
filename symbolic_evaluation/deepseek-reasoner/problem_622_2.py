import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Subtract 1/2
result = pi_over_4 - mp.mpf(1)/2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))