import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the coefficient
sqrt_pi = mp.sqrt(mp.pi)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_sq = gamma_1_4 ** 2
two_power = mp.power(2, mp.mpf(3)/2)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute the rational coefficient part
coefficient = (sqrt_pi * gamma_1_4_sq) / (two_power * gamma_3_4)

# Calculate the hypergeometric function component
hyper_term = mp.hyper([mp.mpf(1)/4], [mp.mpf(3)/4, mp.mpf(1)/2], 4)

# Combine components for final result
result = coefficient * hyper_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))