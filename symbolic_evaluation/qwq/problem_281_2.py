import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(1/4) with high precision
gamma_term = mp.gamma(mp.mpf(1)/4)

# Compute modified Bessel function of the first kind I_{1/4}(4)
bessel_term = mp.besseli(mp.mpf(1)/4, 4)

# Combine all components according to the formula
result = 4 * sqrt_pi * gamma_term * bessel_term

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))