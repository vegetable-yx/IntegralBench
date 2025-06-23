import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute Γ(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Compute Γ(1/4)^4
gamma_quarter_4 = gamma_quarter**4

# Compute Γ(1/4)^8 = (Γ(1/4)^4)^2
gamma_quarter_8 = gamma_quarter_4**2

# Compute π^2
pi_sq = mp.pi**2

# Compute π^4 = (π^2)^2
pi_4 = pi_sq**2

# Compute numerator: Γ(1/4)^8 - 4π^2 Γ(1/4)^4 + 96π^4
numerator = gamma_quarter_8 - 4 * pi_sq * gamma_quarter_4 + 96 * pi_4

# Compute denominator: 3072 π^2
denominator = 3072 * pi_sq

# Compute final result
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))