import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic cosine of 2
cosh_2 = mp.cosh(2)

# Calculate modified Bessel function of first kind I_0(2)
bessel_i0_2 = mp.besseli(0, 2)

# Combine all components using exact mathematical expression
result = mp.pi * sqrt2 * cosh_2 * bessel_i0_2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))