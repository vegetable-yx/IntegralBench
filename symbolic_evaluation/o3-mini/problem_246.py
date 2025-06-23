import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power8 = gamma_val ** 8

# Compute the numerator: 9 * [Gamma(1/4)]^8
numerator = 9 * gamma_power8

# Compute pi squared
pi_squared = mp.pi ** 2

# Compute the denominator: 35840 * pi^2
denominator = 35840 * pi_squared

# Calculate the final result: numerator / denominator
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))