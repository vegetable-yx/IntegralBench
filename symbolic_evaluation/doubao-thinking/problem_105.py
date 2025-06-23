import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 3
sqrt_3 = mp.sqrt(3)

# Calculate π divided by 3
pi_over_3 = mp.pi / 3

# Combine results: √3 - π/3
result = sqrt_3 - pi_over_3

# Output result to exactly 10 decimal places
print(mp.nstr(result, n=10))