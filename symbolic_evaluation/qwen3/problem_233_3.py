import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(1/4) and Gamma(3/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute squared terms for denominator
gamma_1_4_sq = gamma_1_4 ** 2
gamma_3_4_sq = gamma_3_4 ** 2

# Calculate denominator components
denominator = gamma_1_4_sq * gamma_3_4_sq

# Calculate numerator components
numerator = 4 * mp.sqrt(2) * mp.pi

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))