import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the modified Bessel function of the first kind, order 0 at z=1
bessel_value = mp.besseli(0, 1)

# Multiply by 2*pi to get the final result
result = 2 * mp.pi * bessel_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))