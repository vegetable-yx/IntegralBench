import mpmath as mp

# Set the internal decimal precision to 15 digits
mp.dps = 15

# Compute pi to the power of 3/2
pi_power = mp.pi ** (3/2)

# Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply to get the numerator: pi^(3/2) * sqrt(2)
numerator = pi_power * sqrt_two

# Compute the Gamma function at 1/4
gamma_val = mp.gamma(1/4)

# Square the Gamma function to get the denominator
denominator = gamma_val ** 2

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))