import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Gamma(1/4)
gamma_quarter = mp.gamma(mp.mpf(1)/4)

# Compute [Gamma(1/4)]^8
gamma_quarter_eighth = gamma_quarter**8

# Calculate pi squared
pi_squared = mp.pi**2

# Compute denominator: 128 * pi^2
denominator = 128 * pi_squared

# Final result: [Gamma(1/4)]^8 / (128 * pi^2)
result = gamma_quarter_eighth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))