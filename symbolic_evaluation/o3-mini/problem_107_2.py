import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_1_4_sq = gamma_1_4 ** 2

# Compute Gamma(3/4) and square it
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_3_4_sq = gamma_3_4 ** 2

# Calculate the numerator: Γ(1/4)^2 - 2 * Γ(3/4)^2
numerator = gamma_1_4_sq - 2 * gamma_3_4_sq

# Calculate the denominator: 4 * sqrt(2 * pi)
denominator = 4 * mp.sqrt(2 * mp.pi)

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))