import mpmath as mp
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate the numerator (Gamma(1/4))^4
numerator = gamma_1_4**4

# Calculate the denominator 16*pi
denominator = 16 * mp.pi

# Compute final result
result = numerator / denominator

print(mp.nstr(result, n=10))