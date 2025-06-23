import mpmath as mp

# Set internal decimal places for intermediate calculations
mp.dps = 15

# Compute pi to the power of 3/2
pi_power = mp.power(mp.pi, 1.5)

# Compute Gamma(3/4)
gamma_val = mp.gamma(0.75)

# Square the Gamma function value
gamma_sq = gamma_val ** 2

# Compute the denominator: sqrt(2) * [Gamma(3/4)]^2
denominator = mp.sqrt(2) * gamma_sq

# Final result: pi^(3/2) / denominator
result = pi_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))