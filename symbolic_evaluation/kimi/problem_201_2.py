import mpmath as mp
mp.dps = 15

# Compute Bessel function of the first kind J_1(1
bessel_term = mp.besselj(1, 1)

# Compute Struve H function H_1(1)
struve_term = mp.struveh(1, 1)

# Combine terms with pi/2 factor
result = (mp.pi / 2) * (bessel_term + struve_term)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))