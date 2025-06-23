import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_14_8 = gamma_14**8

# Compute pi squared
pi_sq = mp.pi**2

# Calculate denominator: 192 * pi^2
denominator = 192 * pi_sq

# Compute the final result: Gamma^8(1/4) / (192 * pi^2)
result = gamma_14_8 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))