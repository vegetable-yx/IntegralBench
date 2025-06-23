import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf('0.25'))

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_val**4

# Compute sqrt(2 * pi) for the denominator
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Complete denominator: 16 * sqrt(2 * pi)
denominator = 16 * sqrt_2pi

# Final result: Gamma(1/4)^4 / (16 * sqrt(2*pi))
result = gamma_power / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))