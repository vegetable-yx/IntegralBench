import mpmath as mp

mp.dps = 15  # Set decimal precision

# Calculate π²
pi_squared = mp.pi ** 2

# Compute π² / 12
pi_squared_over_12 = pi_squared / 12

# Calculate ln(2)
ln2 = mp.log(2)

# First term: (π² / 12) * ln(2)
term1 = pi_squared_over_12 * ln2

# Calculate ζ(3)
zeta_3 = mp.zeta(3)

# Second term: 2 * ζ(3)
term2 = 2 * zeta_3

# Final result: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))