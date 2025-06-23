import mpmath as mp
mp.dps = 15

# Compute Gamma values at 5/4 and 3/4
gamma_5_4 = mp.gamma(mp.mpf(5)/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Square the Gamma values
gamma_5_4_squared = gamma_5_4 ** 2
gamma_3_4_squared = gamma_3_4 ** 2

# Calculate numerator components
pi_times_gamma_sq = mp.pi * gamma_5_4_squared

# Calculate denominator components
sqrt2 = mp.sqrt(2)
denominator = 2 * sqrt2 * gamma_3_4_squared

# Compute final result
result = pi_times_gamma_sq / denominator

print(mp.nstr(result, n=10))