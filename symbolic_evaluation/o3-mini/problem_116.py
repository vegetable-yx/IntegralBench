import mpmath as mp

# Set decimal places for internal calculations to ensure 10 decimal accuracy
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(0.25)

# Raise Gamma(1/4) to the 8th power
gamma_1_4_power8 = gamma_1_4 ** 8

# Compute pi squared
pi_squared = mp.pi ** 2

# Calculate denominator: 256 * pi^2
denominator = 256 * pi_squared

# Divide numerator by denominator
result = gamma_1_4_power8 / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))