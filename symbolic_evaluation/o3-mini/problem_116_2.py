import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power8 = gamma_1_4**8

# Compute pi squared
pi_squared = mp.pi**2

# Calculate denominator: 1536 * pi^2
denominator = 1536 * pi_squared

# Final result: Gamma(1/4)^8 divided by denominator
result = gamma_power8 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))