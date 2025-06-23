import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute modified Bessel function of the second kind, order 0 at z=3
bessel_k0 = mp.besselk(0, 3)

# Compute modified Bessel function of the second kind, order 1 at z=3
bessel_k1 = mp.besselk(1, 3)

# Square each Bessel function value
k0_sq = bessel_k0**2
k1_sq = bessel_k1**2

# Compute the difference of squares: K0^2(3) - K1^2(3)
diff_sq = k0_sq - k1_sq

# Multiply by 1/8 to get the final result
result = diff_sq / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))