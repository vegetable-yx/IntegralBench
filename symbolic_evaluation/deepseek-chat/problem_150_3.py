import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi^(3/2)
pi_power = mp.pi ** (3/2)

# Compute Gamma(3/4)
gamma_val = mp.gamma(3/4)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute denominator: sqrt(2) * [Gamma(3/4)]^2
denom = sqrt2 * gamma_sq

# Divide numerator by denominator
result = pi_power / denom

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))