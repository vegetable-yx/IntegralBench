import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Compute gamma(1/4)^4 and gamma(1/4)^8 for efficiency
gamma_4 = gamma_val**4
gamma_8 = gamma_4**2

# Compute pi^2 and pi^4
pi_sq = mp.pi**2
pi_4 = pi_sq**2

# Compute numerator: Γ(1/4)^8 - 4π²Γ(1/4)^4 + 16π⁴
numerator = gamma_8 - 4 * pi_sq * gamma_4 + 16 * pi_4

# Compute denominator: 5120π²
denominator = 5120 * pi_sq

# Final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))