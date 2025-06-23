import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(2π)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Calculate Gamma(1/4)
gamma_1over4 = mp.gamma(mp.mpf(1)/4)

# Calculate Bessel function J_{-1/4}(1)
bessel_term = mp.besselj(-mp.mpf(1)/4, 1)

# Combine all components
result = sqrt_2pi * gamma_1over4 * bessel_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))