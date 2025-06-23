import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_sq = gamma_1_4 ** 2

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_3_4_sq = gamma_3_4 ** 2

# Compute the ratio of squared gamma values
gamma_ratio = gamma_1_4_sq / gamma_3_4_sq

# Calculate final result
result = 2 * sqrt_pi * gamma_ratio

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))