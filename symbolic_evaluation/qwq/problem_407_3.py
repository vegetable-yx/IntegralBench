import mpmath as mp
mp.dps = 15

# Calculate square root components
sqrt3 = mp.sqrt(3)
half_sqrt3 = sqrt3 / 2
inv_2sqrt3 = 1 / (2 * sqrt3)

# Compute error function values
erf_term1 = mp.erf(half_sqrt3)
erf_term2 = mp.erf(inv_2sqrt3)

# Calculate the difference between error functions
erf_difference = erf_term1 - erf_term2

# Multiply by π/2 for final result
result = (mp.pi / 2) * erf_difference

print(mp.nstr(result, n=10))