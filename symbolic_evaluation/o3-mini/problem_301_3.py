import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(pi) * Gamma(1/4) / (64 * Gamma(7/4))
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_7_4 = mp.gamma(mp.mpf(7)/4)
sqrt_pi = mp.sqrt(mp.pi)
constant_factor = (sqrt_pi * gamma_1_4) / (64 * gamma_7_4)

# Calculate the digamma terms: 8 * [ψ(7/4) - ψ(1/4)]
psi_1_4 = mp.psi(mp.mpf(1)/4)
psi_7_4 = mp.psi(mp.mpf(7)/4)
digamma_diff = 8 * (psi_7_4 - psi_1_4)

# Calculate the remaining terms: -3π - 8*ln(2)
pi_term = -3 * mp.pi
ln2_term = -8 * mp.log(2)

# Combine the inner expression: 8[ψ(7/4)-ψ(1/4)] - 3π - 8ln(2)
inner_expr = digamma_diff + pi_term + ln2_term

# Multiply the constant factor by the inner expression
result = constant_factor * inner_expr

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))