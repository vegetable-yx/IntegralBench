import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
half_pi = mp.pi / 2

# Compute the result: 2 - π/2
result = 2 - half_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))