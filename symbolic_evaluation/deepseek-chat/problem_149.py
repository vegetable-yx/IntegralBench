import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute pi^(3/2)
pi_power = mp.pi ** (3/2)

# Compute gamma(3/4)
gamma_val = mp.gamma(3/4)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Compute denominator: sqrt(2) * [gamma(3/4)]^2
denominator = mp.sqrt(2) * gamma_sq

# Final result: pi^(3/2) divided by denominator
result = pi_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))