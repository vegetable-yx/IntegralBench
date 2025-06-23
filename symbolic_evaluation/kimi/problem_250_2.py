import mpmath as mp
mp.dps = 15

# Calculate 1/2
half = mp.mpf(1)/2

# Calculate π/2
pi_half = mp.pi/2

# Compute final result: 1/2 - π/2
result = half - pi_half

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))