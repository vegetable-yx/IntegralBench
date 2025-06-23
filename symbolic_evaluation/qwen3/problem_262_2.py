import mpmath as mp
mp.dps = 15

# Calculate Struve H function H_0(2)
struve_term = mp.struveh(0, 2)

# Calculate Bessel function J_0(2)
bessel_term = mp.besselj(0, 2)

# Compute first term: π/4 * H_0(2)
term1 = (mp.pi / 4) * struve_term

# Compute second term: 1/2 * J_0(2)
term2 = 0.5 * bessel_term

# Combine terms for final result
result = term1 - term2

print(mp.nstr(result, n=10))