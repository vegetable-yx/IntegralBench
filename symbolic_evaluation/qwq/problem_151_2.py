import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4) using exact fractional input
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_1_4**4

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute denominator: 8 * sqrt(pi)
denominator = 8 * sqrt_pi

# Calculate final result
result = gamma_power / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))