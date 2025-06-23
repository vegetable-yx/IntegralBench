import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Compute pi
pi_val = mp.pi

# Calculate gamma(1/4)^4
gamma_4 = gamma_val**4

# Calculate gamma(1/4)^8 = (gamma(1/4)^4)^2
gamma_8 = gamma_4**2

# Calculate pi squared
pi_sq = pi_val**2

# Calculate pi^4 = (pi^2)^2
pi_4 = pi_sq**2

# Compute numerator: Γ(1/4)^8 - 8π²Γ(1/4)^4 + 204π⁴
term1 = gamma_8
term2 = 8 * pi_sq * gamma_4
term3 = 204 * pi_4
numerator = term1 - term2 + term3

# Compute denominator: 2048 * π²
denominator = 2048 * pi_sq

# Final result
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))