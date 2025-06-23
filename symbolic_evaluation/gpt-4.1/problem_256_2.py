import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma function values for each fraction
gamma_3_4 = mp.gamma(mp.mpf(3)/4)   # Γ(3/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)   # Γ(5/4)
gamma_7_4 = mp.gamma(mp.mpf(7)/4)   # Γ(7/4)

# Calculate the first term: 16 * Γ(5/4) * Γ(7/4)
term1 = 16 * gamma_5_4 * gamma_7_4

# Calculate the second term: 24 * Γ(3/4) * Γ(5/4)
term2 = 24 * gamma_3_4 * gamma_5_4

# Combine terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))