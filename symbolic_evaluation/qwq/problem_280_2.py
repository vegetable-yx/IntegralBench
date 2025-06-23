import mpmath as mp
mp.dps = 15

# Calculate square root of 6
sqrt6 = mp.sqrt(6)

# Compute sqrt(6)/2 term
sqrt6_over_2 = sqrt6 / 2

# Multiply by pi
pi_term = sqrt6_over_2 * mp.pi

# Calculate modified Bessel function I_0(3)
bessel_term = mp.besseli(0, 3)

# Combine all components for final result
result = pi_term * bessel_term

print(mp.nstr(result, n=10))