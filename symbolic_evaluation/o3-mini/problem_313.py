import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_quarter_eighth = gamma_quarter**8

# Compute pi squared
pi_squared = mp.pi**2

# Calculate denominator: 192 * pi^2
denominator = 192 * pi_squared

# Compute the final result: Gamma(1/4)^8 / (192 * pi^2)
result = gamma_quarter_eighth / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))