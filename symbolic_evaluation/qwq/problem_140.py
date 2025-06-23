import mpmath as mp
mp.dps = 15  # Set decimal places for calculations

# Compute modified Bessel function of the first kind of order 1 at 2
bessel_i1 = mp.besseli(1, 2)

# Multiply by 2 to get the final result
result = 2 * bessel_i1

print(mp.nstr(result, n=10))