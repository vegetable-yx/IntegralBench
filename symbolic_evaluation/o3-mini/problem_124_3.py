import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf('0.25'))

# Compute powers of Gamma(1/4) needed for the expression
gamma_4 = gamma_1_4**4  # Gamma(1/4)^4
gamma_8 = gamma_4**2    # Gamma(1/4)^8

# Compute powers of pi
pi = mp.pi
pi_sq = pi**2           # pi^2
pi_4 = pi_sq**2         # pi^4

# Compute the three terms in the numerator
term1 = gamma_8          # Γ(1/4)^8
term2 = 8 * pi_sq * gamma_4  # 8π²Γ(1/4)^4
term3 = -64 * pi_4       # -64π^4

# Combine terms for numerator
numerator = term1 + term2 + term3

# Compute denominator: 512 * π²
denominator = 512 * pi_sq

# Final expression: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))