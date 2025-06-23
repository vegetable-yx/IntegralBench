import mpmath as mp

# Set precision
mp.dps = 15

# Compute the gamma function values
gamma_14 = mp.gamma(1/4)
gamma_34 = mp.gamma(3/4)

# Compute pi^(3/2) = pi * sqrt(pi)
pi_sqrt = mp.sqrt(mp.pi)
pi_power = mp.pi * pi_sqrt  # This is pi^(3/2)

# Compute numerator: pi^(3/2) * [Gamma(1/4)]^2
numerator = pi_power * (gamma_14 ** 2)

# Compute denominator: 4 * [Gamma(3/4)]^2
denominator = 4 * (gamma_34 ** 2)

# Final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))