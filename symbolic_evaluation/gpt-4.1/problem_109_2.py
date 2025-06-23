import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the numerator: sqrt(pi) * Gamma(1/4)
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
gamma_1_4 = mp.gamma(1/4)  # Gamma function at 1/4
numerator = sqrt_pi * gamma_1_4

# Compute the denominator: 2 * [Gamma(7/8)]^2
gamma_7_8 = mp.gamma(7/8)  # Gamma function at 7/8
denominator = 2 * (gamma_7_8 ** 2)

# Compute the final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))