import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel functions of the first kind
J0_2 = mp.besselj(0, 2)
J2_2 = mp.besselj(2, 2)

# Compute trigonometric terms
sin2 = mp.sin(2)
cos2 = mp.cos(2)

# Calculate numerator components
term1 = 2 * J0_2
term2 = mp.pi * J2_2
term3 = -2 * sin2
term4 = -cos2
term5 = 1

# Sum all numerator terms
numerator = term1 + term2 + term3 + term4 + term5

# Compute final result by dividing by pi
result = numerator / mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))