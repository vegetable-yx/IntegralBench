import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the Bessel function of the first kind J_{0.5}(2.0)
bessel_value = mp.besselj(0.5, 2.0)

# Square the Bessel function result
bessel_squared = bessel_value ** 2

# Calculate the coefficient 2/8
coefficient = mp.mpf(2) / 8

# Compute the final result by multiplying coefficient with squared Bessel
result = coefficient * bessel_squared

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))