import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π/6
pi_over_6 = mp.pi / 6

# Compute √3
sqrt_3 = mp.sqrt(3)

# Compute √3/8
sqrt_3_over_8 = sqrt_3 / 8

# Sum the two components: π/6 + √3/8
result = pi_over_6 + sqrt_3_over_8

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))