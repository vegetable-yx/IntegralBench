import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Compute gamma functions for required fractions
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Gamma(1/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Gamma(3/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)  # Gamma(5/4)

# Compute squares of gamma functions
gamma_1_4_sq = gamma_1_4 ** 2     # [Gamma(1/4)]^2
gamma_3_4_sq = gamma_3_4 ** 2     # [Gamma(3/4)]^2
gamma_5_4_sq = gamma_5_4 ** 2     # [Gamma(5/4)]^2

# Compute numerator components
inner_sum = gamma_1_4_sq + 4 * gamma_3_4_sq  # [Gamma(1/4)]^2 + 4[Gamma(3/4)]^2
pi_power = mp.pi ** (mp.mpf(3)/2)  # pi^(3/2)
numerator = pi_power * inner_sum   # pi^(3/2) * (above sum)

# Compute denominator
denominator = 64 * gamma_5_4_sq   # 64 * [Gamma(5/4)]^2

# Final result
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))