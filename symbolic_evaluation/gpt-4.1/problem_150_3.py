import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_sq = gamma_1_4**2

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the denominator: 4 * sqrt(pi)
denominator = 4 * sqrt_pi

# Divide squared gamma by denominator to get final result
result = gamma_sq / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))