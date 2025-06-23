import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the numerator: 2 * sqrt(2) * pi^(3/2)
sqrt2 = mp.sqrt(2)  # Compute square root of 2
pi_power = mp.pi ** (3/2)  # Compute pi raised to the power of 3/2
numerator = 2 * sqrt2 * pi_power  # Combine to get numerator

# Calculate the denominator: [Gamma(1/4)]^2
gamma_val = mp.gamma(1/4)  # Compute Gamma(1/4)
denominator = gamma_val ** 2  # Square the Gamma value

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))