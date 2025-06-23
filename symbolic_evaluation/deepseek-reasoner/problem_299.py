import mpmath as mp
mp.dps = 15

# Calculate Gamma(1/4) with high precision
gamma_1over4 = mp.gamma(mp.mpf(1)/4)

# Calculate Gamma(3/4) with high precision
gamma_3over4 = mp.gamma(mp.mpf(3)/4)

# Compute the ratio of Gamma functions
gamma_ratio = gamma_1over4 / gamma_3over4

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Combine all components for final result
result = 8 * sqrt_pi * gamma_ratio

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))