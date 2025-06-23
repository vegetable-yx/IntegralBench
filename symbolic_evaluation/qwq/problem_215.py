import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma function values
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Calculate ratio of Gamma functions
gamma_ratio = gamma_3_4 / gamma_5_4

# Compute Bessel function of the first kind at 1/4 order with argument 1/2
bessel_j_1_4 = mp.besselj(mp.mpf(1)/4, mp.mpf(1)/2)

# Combine all components for final result
result = sqrt_pi * gamma_ratio * bessel_j_1_4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))