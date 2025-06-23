import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Compute pi raised to the power of 3/2
pi_power = mp.pi ** (3/2)

# Compute the numerator: sqrt(2) * π^(3/2)
numerator = sqrt2 * pi_power

# Compute Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Square the Gamma function
gamma_sq = gamma_val ** 2

# Compute the denominator: [Gamma(3/4)]^2
denominator = gamma_sq

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))