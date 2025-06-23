import mpmath as mp
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute the fourth power of Gamma(1/4)
gamma_power = gamma_1_4**4

# Calculate the constant denominator 16*pi
denominator = 16 * mp.pi

# Combine components to get final result
result = gamma_power / denominator

print(mp.nstr(result, n=10))