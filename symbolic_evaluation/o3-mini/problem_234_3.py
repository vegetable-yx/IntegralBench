import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Compute (sqrt(2) + 1)
numerator_factor = sqrt2 + 1

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function
gamma_sq = gamma_val ** 2

# Compute the denominator: 8 * sqrt(pi)
denominator = 8 * mp.sqrt(mp.pi)

# Combine all parts to compute the result
result = (numerator_factor * gamma_sq) / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))