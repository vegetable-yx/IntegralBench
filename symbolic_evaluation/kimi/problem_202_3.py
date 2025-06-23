import mpmath as mp
mp.dps = 15

# Compute Struve H function of order 1 at z=1
struve_h = mp.struveh(1, 1)

# Compute Bessel J function of order 1 at z=1
bessel_j = mp.besselj(1, 1)

# Calculate the final result using the analytical expression
result = (mp.pi / 2) * (struve_h - bessel_j)

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))