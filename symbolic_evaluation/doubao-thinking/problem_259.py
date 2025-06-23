import mpmath as mp

mp.dps = 15  # Compute Bessel function of the first kind J0(1)
bessel_term = mp.besselj(0, 1)

# Compute Struve function H0(1)
struve_term = mp.struveh(0, 1)

# Calculate the final result using π*(J0(1) - H0(1))
result = mp.pi * (bessel_term - struve_term)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))