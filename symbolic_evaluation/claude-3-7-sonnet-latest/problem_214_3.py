import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath constant
pi_value = mp.pi

# Calculate Bessel function of the first kind, order 0 at z=1
bessel_value = mp.besselj(0, 1)

# Multiply pi by the Bessel function value
result = pi_value * bessel_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))