import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the constant term: 1/4
constant_term = mp.mpf(1)/4

# Compute Bessel function J0 at 2
bessel_j0 = mp.besselj(0, 2)

# Calculate the numerator: 2 + π
numerator = 2 + mp.pi

# Compute the fraction: (2 + π)/8
fraction = numerator / 8

# Multiply Bessel J0(2) by the fraction
bessel_product = bessel_j0 * fraction

# Final result: constant_term minus bessel_product
result = constant_term - bessel_product

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))