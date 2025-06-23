import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate hyperbolic functions
sinh3 = mp.sinh(3)
cosh3 = mp.cosh(3)

# Calculate components of the numerator
term1 = 3 * sinh3
sqrt3_pi = mp.sqrt(3) * mp.pi
term2 = sqrt3_pi * cosh3

# Combine terms and divide by 2
numerator = term1 + term2
result = numerator / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))