import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator 2 * e
denominator = 2 * mp.e

# Compute final result (sqrt(pi)/(2e))
result = sqrt_pi / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))