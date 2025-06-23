import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 8th power
gamma_eighth = gamma_val**8

# Compute pi squared
pi_squared = mp.pi**2

# Calculate denominator: 960 * pi^2
denominator = 960 * pi_squared

# Final result: Gamma(1/4)^8 / (960 * pi^2)
result = gamma_eighth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))