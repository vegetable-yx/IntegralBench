import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate denominator component: 2 * sqrt(2)
sqrt2 = mp.sqrt(2)
denominator = 2 * sqrt2

# Compute the final result: pi divided by (2*sqrt(2))
result = mp.pi / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))