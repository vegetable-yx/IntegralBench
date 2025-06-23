import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(1/4)^4 and Gamma(1/4)^8
gamma_1_4_4 = gamma_1_4**4
gamma_1_4_8 = gamma_1_4_4**2

# Get pi constant
pi_val = mp.pi

# Compute numerator: Gamma(1/4)^8 - 16*pi*Gamma(1/4)^4 + 64*pi^2
term1 = gamma_1_4_8
term2 = 16 * pi_val * gamma_1_4_4
term3 = 64 * pi_val**2
numerator = term1 - term2 + term3

# Compute denominator: 1024 * pi^2
denominator = 1024 * pi_val**2

# Final result: numerator / denominator
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))