import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/6 component
pi_over_6 = mp.pi / 6

# Calculate √3 component and divide by 8
sqrt3_over_8 = mp.sqrt(3) / 8

# Sum the two components
result = pi_over_6 + sqrt3_over_8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))