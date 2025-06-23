import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

x = 2  # Upper limit of integration

# Compute modified Bessel functions of the second kind
K0 = mp.besselk(0, x)
K1 = mp.besselk(1, x)

# Compute modified Struve functions
L0 = mp.struvel(0, x)
L1 = mp.struvel(1, x)

# Calculate the terms from the analytical solution formula
combined_term = K1 * L0 + K0 * L1
product_term = x * combined_term

# Final result calculation using the analytical expression
result = (mp.pi/2) * (1 - product_term)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))