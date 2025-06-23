import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_val**4

# Compute the constant pi
pi_val = mp.pi

# Calculate the denominator: 16 * sqrt(2 * pi)
denominator = 16 * mp.sqrt(2 * pi_val)

# Compute the final result: [Gamma(1/4)^4] / denominator
result = gamma_power / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))