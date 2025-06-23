import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute modified Bessel function of the first kind I_0(2)
i0 = mp.besseli(0, 2)

# Compute modified Bessel function of the second kind K_0(2)
k0 = mp.besselk(0, 2)

# Calculate the product of Bessel functions
product = i0 * k0

# Compute 1 minus the product term
term = 1 - product

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))