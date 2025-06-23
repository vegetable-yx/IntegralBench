import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the Bessel function of the first kind J_2(2)
bessel_j2 = mp.besselj(2, 2)

# Multiply by 2 to get the final result
result = 2 * bessel_j2

print(mp.nstr(result, n=10))