import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate first term components
a1 = mp.mpf(1)/25   # 1/25
b1 = mp.mpf(21)/20  # 21/20
c1 = a1 + b1        # 1/25 + 21/20

# Compute Gamma functions for first term
gamma_a1 = mp.gamma(a1)
gamma_b1 = mp.gamma(b1)
gamma_c1 = mp.gamma(c1)

# Construct first term: (1/25) * [Γ(1/25)*Γ(21/20)] / Γ(1/25 + 21/20)
term1 = (mp.mpf(1)/25) * (gamma_a1 * gamma_b1) / gamma_c1

# Calculate second term components
a2 = mp.mpf(1)/20   # 1/20
b2 = mp.mpf(26)/25  # 26/25
c2 = a2 + b2        # 1/20 + 26/25

# Compute Gamma functions for second term
gamma_a2 = mp.gamma(a2)
gamma_b2 = mp.gamma(b2)
gamma_c2 = mp.gamma(c2)

# Construct second term: (1/20) * [Γ(1/20)*Γ(26/25)] / Γ(1/20 + 26/25)
term2 = (mp.mpf(1)/20) * (gamma_a2 * gamma_b2) / gamma_c2

# Combine terms: result = term1 - term2
result = term1 - term2

# Print final result rounded to 10 decimal places
print(mp.nstr(result, n=10))