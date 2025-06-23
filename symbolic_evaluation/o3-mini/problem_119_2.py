import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_val ** 8

# Compute pi squared
pi_squared = mp.pi ** 2

# Denominator: 1024 * pi^2
denominator = 1024 * pi_squared

# Final result: [Gamma(1/4)^8] / [1024 * pi^2]
result = gamma_power / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))