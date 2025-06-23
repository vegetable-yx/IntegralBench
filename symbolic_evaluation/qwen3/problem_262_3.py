import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute components of the closed-form solution
sqrt_pi = mp.sqrt(mp.pi)
j0 = mp.besselj(0, 1)  # Bessel J_0 at 1
j1 = mp.besselj(1, 1)  # Bessel J_1 at 1

# Calculate the product of Bessel functions
bessel_product = j0 * j1

# Combine all terms according to the analytical solution
result = (sqrt_pi * bessel_product) / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))