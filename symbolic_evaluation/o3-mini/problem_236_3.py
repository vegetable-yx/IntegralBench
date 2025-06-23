import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_sq = gamma_val ** 2

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute (sqrt(2) + 1)
sqrt2_plus_one = sqrt2 + 1

# Multiply Gamma(1/4)^2 by (sqrt(2) + 1)
numerator = gamma_sq * sqrt2_plus_one

# Compute denominator: 4 * sqrt(2 * pi)
denom_factor1 = 2 * mp.pi
denom_factor2 = mp.sqrt(denom_factor1)
denominator = 4 * denom_factor2

# Compute final result
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))