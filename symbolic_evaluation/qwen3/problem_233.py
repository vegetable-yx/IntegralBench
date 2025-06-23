import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(1/4)

# Square the Gamma(1/4) value
gamma_squared = gamma_1_4 ** 2

# Calculate the numerator: 4*sqrt(2)*Gamma(1/4)^2
numerator = 4 * mp.sqrt(2) * gamma_squared

# Calculate the denominator: sqrt(pi)
denominator = mp.sqrt(mp.pi)

# Compute the final result
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))