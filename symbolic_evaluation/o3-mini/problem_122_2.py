import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi raised to the power of 3/2
pi_power = mp.pi ** (3/2)

# Calculate Gamma(1/4) and square it
gamma_1_4 = mp.gamma(1/4)
gamma_1_4_sq = gamma_1_4 ** 2

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(3/4)
gamma_3_4_sq = gamma_3_4 ** 2

# Numerator: pi^{3/2} * [Gamma(1/4)]^2
numerator = pi_power * gamma_1_4_sq

# Denominator: 16 * [Gamma(3/4)]^2
denominator = 16 * gamma_3_4_sq

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))