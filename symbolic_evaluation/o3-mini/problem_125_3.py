import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Compute gamma(1/4) once and reuse
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Precompute gamma_14 raised to powers used multiple times
gamma_14_8 = gamma_14**8
gamma_14_16 = gamma_14**16

# Compute powers of pi
pi_sq = mp.pi**2
pi_4th = mp.pi**4

# Calculate numerator terms
term1 = gamma_14_16
term2 = 192 * pi_sq * gamma_14_8
term3 = 1024 * pi_4th

# Combine numerator terms
numerator = term1 + term2 + term3

# Calculate denominator
denom_factor1 = 2688
denom_factor2 = mp.sqrt(2)
denom_factor3 = pi_sq * gamma_14_8
denominator = denom_factor1 * denom_factor2 * denom_factor3

# Compute the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))