import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute I_0(1) - modified Bessel function of the first kind, order 0 at 1
bessel_value = mp.besseli(0, 1)

# Multiply by pi
result = mp.pi * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))