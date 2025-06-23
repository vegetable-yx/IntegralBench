import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate gamma(1/4) and gamma(3/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Square each gamma value
gamma_1_4_sq = gamma_1_4 ** 2
gamma_3_4_sq = gamma_3_4 ** 2

# Compute the difference: Γ(1/4)^2 - Γ(3/4)^2
diff_sq = gamma_1_4_sq - gamma_3_4_sq

# Compute sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Numerator: sqrt(pi) * (Γ(1/4)^2 - Γ(3/4)^2)
numerator = sqrt_pi * diff_sq

# Denominator: 8 * sqrt(2)
denominator = 8 * mp.sqrt(2)

# Final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))