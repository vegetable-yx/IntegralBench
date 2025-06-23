import mpmath as mp
mp.dps = 15

# Compute sqrt(2)
sqrt_2 = mp.sqrt(2)

# Compute pi^(3/2)
pi_power = mp.pi ** 1.5

# Calculate numerator: 4 * sqrt(2) * pi^(3/2)
numerator = 4 * sqrt_2 * pi_power

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Square Gamma(3/4) for denominator
denominator = gamma_3_4 ** 2

# Final result
result = numerator / denominator

print(mp.nstr(result, n=10))