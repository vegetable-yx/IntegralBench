import mpmath as mp
mp.dps = 15

# Calculate π/2
pi_half = mp.pi / 2

# Calculate cosine integral Ci(2)
ci_2 = mp.ci(2)

# Combine results
result = pi_half - ci_2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))