import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Calculate Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_quarter_power8 = gamma_quarter**8

# Calculate pi squared
pi_squared = mp.pi**2

# Compute denominator: 2048 * pi^2
denominator = 2048 * pi_squared

# Final result: [Gamma(1/4)^8] / [2048 * pi^2]
result = gamma_quarter_power8 / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))