import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_quarter_power8 = gamma_quarter**8

# Compute pi squared
pi_squared = mp.pi**2

# Calculate denominator: 1024 * pi^2
denominator = 1024 * pi_squared

# Final result: Gamma(1/4)^8 / (1024 * pi^2)
result = gamma_quarter_power8 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))