import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma value
gamma_sq = gamma_val ** 2

# Compute the constant factor: sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the entire expression: (pi/2) * [Gamma(1/4)]^2 / sqrt(pi)
# This simplifies to: (pi / (2 * sqrt(pi))) * gamma_sq = (sqrt(pi)/2) * gamma_sq
result = (mp.sqrt(mp.pi) / 2 * gamma_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))