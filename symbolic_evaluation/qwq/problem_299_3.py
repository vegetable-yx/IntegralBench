import mpmath as mp
mp.dps = 15

# Compute digamma values at specified points
psi_1_4 = mp.psi(mp.mpf(1)/4)
psi_3_4 = mp.psi(mp.mpf(3)/4)
psi_5_4 = mp.psi(mp.mpf(5)/4)

# Combine digamma terms
psi_combination = psi_1_4 - 2*psi_3_4 + psi_5_4

# Calculate pi^(3/2) term
pi_power = mp.pi ** (mp.mpf(3)/2)

# Compute numerator components
numerator = pi_power * psi_combination

# Calculate Gamma(3/4) and 2^(1/4) terms
gamma_34 = mp.gamma(mp.mpf(3)/4)
gamma_squared = gamma_34 ** 2
two_power = 2 ** (mp.mpf(1)/4)

# Compute denominator
denominator = two_power * gamma_squared

# Final calculation
result = numerator / denominator

print(mp.nstr(result, n=10))