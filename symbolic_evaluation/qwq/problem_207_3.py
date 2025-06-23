import mpmath as mp
mp.dps = 15

# Calculate denominator component: 2 * sqrt(2)
denominator = 2 * mp.sqrt(2)

# Compute final result: pi divided by (2*sqrt(2))
result = mp.pi / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))