import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute modified Bessel function I_{1/2}(1)
bessel_term = mp.besseli(0.5, 1)

# Square the Bessel function result
bessel_squared = bessel_term ** 2

# Combine all components
result = 2 * sqrt2 * mp.pi * bessel_squared

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))