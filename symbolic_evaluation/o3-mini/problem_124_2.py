import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute Γ(1/4)
gamma_14 = mp.gamma(0.25)

# Compute Γ(1/4)^4
gamma_14_4 = gamma_14**4

# Compute Γ(1/4)^8 = (Γ(1/4)^4)^2
gamma_14_8 = gamma_14_4**2

# Compute π and π^2
pi_val = mp.pi
pi_sq = pi_val**2

# Compute π^4 = (π^2)^2
pi_4th = pi_sq**2

# Compute numerator: Γ(1/4)^8 + 32π^2 Γ(1/4)^4 - 512π^4
numerator = gamma_14_8 + 32 * pi_sq * gamma_14_4 - 512 * pi_4th

# Compute denominator: 1024 π^2
denominator = 1024 * pi_sq

# Final result
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))