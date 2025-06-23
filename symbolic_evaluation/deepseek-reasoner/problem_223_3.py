import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^2/2
pi_squared_over_2 = mp.pi**2 / 2

# Calculate 4*Catalan's constant
four_g = 4 * mp.catalan

# Combine terms for final result
result = pi_squared_over_2 - four_g

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))