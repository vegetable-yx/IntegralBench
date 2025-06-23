import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi/2
half_pi = mp.pi / 2

# Compute the Bessel function of the first kind J0(1)
bessel_value = mp.besselj(0, 1)

# Multiply to get the final result
result = half_pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))