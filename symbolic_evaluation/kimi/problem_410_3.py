import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator component 2*e
denominator = 2 * mp.e

# Compute final result by dividing sqrt(pi) by (2e)
result = sqrt_pi / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))