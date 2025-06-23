import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate 1/2 as a mpmath float
half = mp.mpf(1) / 2

# Combine results: π/4 - 1/2
result = pi_over_4 - half

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))