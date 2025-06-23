import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: (1/25) * [Γ(1/25) * Γ(21/20) / Γ(1/25 + 21/20)]
a1 = mp.mpf(1)/25
b1 = mp.mpf(21)/20
gamma_a1 = mp.gamma(a1)
gamma_b1 = mp.gamma(b1)
gamma_sum1 = mp.gamma(a1 + b1)
term1 = (mp.mpf(1)/25) * (gamma_a1 * gamma_b1) / gamma_sum1

# Calculate the second term: (1/20) * [Γ(1/20) * Γ(26/25) / Γ(1/20 + 26/25)]
a2 = mp.mpf(1)/20
b2 = mp.mpf(26)/25
gamma_a2 = mp.gamma(a2)
gamma_b2 = mp.gamma(b2)
gamma_sum2 = mp.gamma(a2 + b2)
term2 = (mp.mpf(1)/20) * (gamma_a2 * gamma_b2) / gamma_sum2

# Compute final result as the difference
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))