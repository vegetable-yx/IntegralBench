import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Calculate the Bessel function of the first kind of order 1/4 at x=1/2
bessel_val = mp.besselj(mp.mpf(1)/4, mp.mpf(1)/2)

# Multiply the components together
result = sqrt_pi * gamma_val * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))