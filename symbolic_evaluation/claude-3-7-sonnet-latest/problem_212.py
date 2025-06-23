import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the value of pi using mpmath constant
pi_value = mp.pi

# Compute the Bessel function of the first kind of order 1 at 1
bessel_value = mp.besselj(1, 1)

# Multiply pi by the Bessel function value
result = pi_value * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))