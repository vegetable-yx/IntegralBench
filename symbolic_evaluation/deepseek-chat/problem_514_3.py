import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/6
pi_over_6 = mp.pi / 6

# Calculate √3
sqrt_3 = mp.sqrt(3)

# Calculate √3/8
sqrt3_over_8 = sqrt_3 / 8

# Sum the two terms: π/6 + √3/8
result = pi_over_6 + sqrt3_over_8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))