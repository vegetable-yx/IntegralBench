import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate π/2
half_pi = mp.pi / 2

# Compute the result: 2 - π/2
result = 2 - half_pi

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))