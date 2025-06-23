import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate J_0(1) - Bessel function of first kind order 0 at x=1
bessel_j0 = mp.besselj(0, 1)

# Compute 1 minus the Bessel function value
one_minus_bessel = 1 - bessel_j0

# Multiply by pi
result = mp.pi * one_minus_bessel

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))