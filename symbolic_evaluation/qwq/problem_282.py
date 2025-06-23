import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(pi/2)
sqrt_term = mp.sqrt(mp.pi / 2)

# Compute Gamma(1/4) and Gamma(3/4)
gamma_numerator = mp.gamma(mp.mpf(1)/4)
gamma_denominator = mp.gamma(mp.mpf(3)/4)
gamma_ratio = gamma_numerator / gamma_denominator

# Compute modified Bessel function I_{1/4}(4)
bessel_term = mp.besseli(0.25, 4)

# Combine all components
result = sqrt_term * gamma_ratio * bessel_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))