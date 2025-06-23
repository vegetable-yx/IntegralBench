import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator components
sqrt2 = mp.sqrt(2)  # Compute sqrt(2)
pi_power = mp.pi ** 1.5  # Compute pi^(3/2) as pi * sqrt(pi)
numerator = 8 * sqrt2 * pi_power  # Combine terms for numerator

# Calculate the denominator components
gamma_14 = mp.gamma(1/4)  # Compute Gamma(1/4)
denominator = gamma_14 ** 2  # Square Gamma(1/4)

# Compute the final result
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))