import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power8 = gamma_val**8

# Calculate pi squared
pi_sq = mp.pi**2

# Compute denominator: 128 * pi^2
denominator = 128 * pi_sq

# Compute the final result: [Gamma(1/4)^8] / [128 * pi^2]
result = gamma_power8 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))