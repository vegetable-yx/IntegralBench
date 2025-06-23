import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/3)
gamma_one_third = mp.gamma(mp.mpf(1)/3)

# Raise Gamma(1/3) to the 6th power
gamma_sixth = gamma_one_third ** 6

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Compute sqrt(3)
sqrt3 = mp.sqrt(3)

# Numerator: 3 * sqrt(3) * pi^3
numerator = 3 * sqrt3 * pi_cubed

# Denominator: 32 * Gamma^6(1/3)
denominator = 32 * gamma_sixth

# Final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))