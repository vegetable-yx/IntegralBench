import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Compute powers of gamma(1/4) to avoid repeated calculations
gamma_14_4 = gamma_14**4  # gamma(1/4)^4
gamma_14_8 = gamma_14_4**2  # gamma(1/4)^8

# Compute powers of pi
pi = mp.pi
pi_sq = pi**2  # pi^2
pi_4 = pi_sq**2  # pi^4

# Calculate the numerator: gamma(1/4)^8 - 16*pi^2*gamma(1/4)^4 + 16*pi^4
term1 = gamma_14_8
term2 = 16 * pi_sq * gamma_14_4
term3 = 16 * pi_4
numerator = term1 - term2 + term3

# Calculate the denominator: 128 * pi^2
denominator = 128 * pi_sq

# Final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))