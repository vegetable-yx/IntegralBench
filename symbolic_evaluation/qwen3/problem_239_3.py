import mpmath as mp
mp.dps = 15

# Compute modified Bessel functions of first kind
i0 = mp.besseli(0, 2)
i1 = mp.besseli(1, 2)

# Compute modified Bessel functions of second kind
k0 = mp.besselk(0, 2)
k1 = mp.besselk(1, 2)

# Calculate individual product terms
term1 = i0 * k0
term2 = i1 * k1

# Combine terms and compute final result
sum_terms = term1 + term2
result = 0.5 * sum_terms

print(mp.nstr(result, n=10))