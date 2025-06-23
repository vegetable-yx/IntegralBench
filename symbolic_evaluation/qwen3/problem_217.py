import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 for internal calculations

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the Gamma function at 1/4
gamma_val = mp.gamma(mp.mpf(1)/4)

# Compute the Bessel function of the first kind of order -1/4 at 1
bessel_val = mp.besselj(-mp.mpf(1)/4, 1)

# Multiply all components together
result = sqrt_pi * gamma_val * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))