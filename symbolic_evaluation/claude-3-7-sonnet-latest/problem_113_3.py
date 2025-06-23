import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^(5/2) = pi^2 * sqrt(pi)
pi = mp.pi
pi_squared = mp.power(pi, 2)
sqrt_pi = mp.sqrt(pi)
pi_to_5_2 = pi_squared * sqrt_pi

# Compute Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Square the Gamma value
gamma_sq = mp.power(gamma_val, 2)

# Compute numerator: 4 * pi^(5/2) * [Gamma(3/4)]^2
numerator = 4 * pi_to_5_2 * gamma_sq

# Divide by 3 to get final result
result = numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))