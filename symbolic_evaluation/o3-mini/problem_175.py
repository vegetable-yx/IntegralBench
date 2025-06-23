import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Calculate pi raised to the power of 3/2
pi_power = mp.pi ** (3/2)

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(3/4)
gamma_3_4_sq = gamma_3_4 ** 2

# Calculate Gamma(5/4) and square it
gamma_5_4 = mp.gamma(5/4)
gamma_5_4_sq = gamma_5_4 ** 2

# Compute the denominator: 32 * [Gamma(5/4)]^2
denominator = 32 * gamma_5_4_sq

# Compute the numerator: pi^{3/2} * [Gamma(3/4)]^2
numerator = pi_power * gamma_3_4_sq

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))