import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/3)
gamma_one_third = mp.gamma(1/3)

# Cube the Gamma(1/3) value
gamma_one_third_cubed = gamma_one_third ** 3

# Calculate Gamma(5/6)
gamma_five_sixth = mp.gamma(5/6)

# Compute the denominator: 12 * Gamma(5/6)
denominator = 12 * gamma_five_sixth

# Combine numerator and denominator
numerator = sqrt_pi * gamma_one_third_cubed
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))