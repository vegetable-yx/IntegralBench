import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(1/4)
gamma_value = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(1/4)^4
gamma_power = gamma_value**4

# Calculate pi squared
pi_sq = mp.pi**2

# Compute denominator 24*pi^2
denominator = 24 * pi_sq

# Calculate final result
result = gamma_power / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))