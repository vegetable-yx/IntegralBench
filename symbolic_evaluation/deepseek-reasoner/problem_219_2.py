import mpmath as mp
mp.dps = 15

# Compute Bessel function term J_1(1)
bessel_term = mp.besselj(1, 1)

# Compute Struve function term H_1(1)
struve_term = mp.struveh(1, 1)

# Combine terms with pi/2 factor
integral_value = (mp.pi / 2) * (bessel_term + struve_term)

# Multiply by 2*sqrt(2) for final result
result = 2 * mp.sqrt(2) * integral_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))