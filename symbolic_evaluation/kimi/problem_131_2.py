import mpmath as mp
mp.dps = 15

# Calculate the argument for the Bessel function
sqrt_term = mp.sqrt(2.0)
bessel_arg = 2 * sqrt_term

# Compute modified Bessel function of the first kind with order -1/4
bessel_result = mp.besseli(-0.25, bessel_arg)

# Multiply by 8/3 coefficient using exact fractional arithmetic
coefficient = mp.mpf(8)/3
result = coefficient * bessel_result

print(mp.nstr(result, n=10))