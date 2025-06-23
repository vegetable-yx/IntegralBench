import mpmath as mp
mp.dps = 15

# Calculate sqrt(6)
sqrt6 = mp.sqrt(6)

# Multiply sqrt(6) by pi
sqrt6_pi = sqrt6 * mp.pi

# Divide by 2 to get the coefficient term
coefficient = sqrt6_pi / 2

# Compute the modified Bessel function I_0(3)
bessel_i0_3 = mp.besseli(0, 3)

# Multiply coefficient by Bessel function result
result = coefficient * bessel_i0_3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))