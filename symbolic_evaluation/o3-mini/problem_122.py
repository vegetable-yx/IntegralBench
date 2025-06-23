import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Numerator: 5 * [Gamma(1/4)]^8
numerator = 5 * gamma_power

# Compute pi squared
pi_sq = mp.pi**2

# Denominator: 6144 * pi^2
denominator = 6144 * pi_sq

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))