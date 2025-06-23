import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(1/4)^4 and Gamma(1/4)^8
gamma_14_4 = gamma_14**4
gamma_14_8 = gamma_14**8

# Compute pi and its powers
pi_val = mp.pi
pi_sq = pi_val**2
pi_4 = pi_val**4

# Compute the numerator: Gamma(1/4)^8 + 16*pi^2*Gamma(1/4)^4 - 192*pi^4
term1 = gamma_14_8
term2 = 16 * pi_sq * gamma_14_4
term3 = 192 * pi_4
numerator = term1 + term2 - term3

# Compute the denominator: 6144 * sqrt(2) * pi
sqrt2 = mp.sqrt(2)
denominator = 6144 * sqrt2 * pi_val

# Final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))