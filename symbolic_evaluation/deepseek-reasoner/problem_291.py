import mpmath as mp
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(1/4)^4
gamma_power = gamma_1_4**4

# Calculate denominator 32*π
denominator = 32 * mp.pi

# Final result calculation
result = gamma_power / denominator

print(mp.nstr(result, n=10))