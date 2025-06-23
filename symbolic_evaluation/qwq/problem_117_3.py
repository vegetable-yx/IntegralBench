import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Calculate Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Compute the ratio of Gamma functions (Γ(1/4)^4)/(Γ(3/4)^2)
gamma_ratio = (gamma_14**4) / (gamma_34**2)

# Calculate the pi^4/256 term
pi_term = (mp.pi**4) / 256

# Combine terms to get final result
result = pi_term * gamma_ratio

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))