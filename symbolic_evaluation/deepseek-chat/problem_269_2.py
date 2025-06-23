import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/12
pi_over_12 = mp.pi / 12

# Calculate √3
sqrt_3 = mp.sqrt(3)

# Calculate √3/8
sqrt3_over_8 = sqrt_3 / 8

# Calculate 1/8
one_eighth = mp.mpf(1) / 8

# Combine terms: π/12 - √3/8 + 1/8
result = pi_over_12 - sqrt3_over_8 + one_eighth

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))