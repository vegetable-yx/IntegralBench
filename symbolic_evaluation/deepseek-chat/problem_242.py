import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/3)
gamma_one_third = mp.gamma(1/3)

# Compute gamma(1/3) raised to the 6th power
gamma_cubed = gamma_one_third ** 6

# Calculate the numerator: 3 * [gamma(1/3)]^6
numerator = 3 * gamma_cubed

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate the denominator: 32 * pi^2
denominator = 32 * pi_squared

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))