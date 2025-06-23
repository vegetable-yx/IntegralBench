import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(1/4)

# Raise Gamma(1/4) to the fourth power
gamma_power = gamma_val**4

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator: 16 * sqrt(pi)
denominator = 16 * sqrt_pi

# Divide numerator by denominator
result = gamma_power / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))