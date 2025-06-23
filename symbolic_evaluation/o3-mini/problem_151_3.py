import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 4th power
gamma_fourth_power = gamma_val**4

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator: 16 * sqrt(pi)
denominator = 16 * sqrt_pi

# Final result: (gamma(1/4)^4 / (16 * sqrt(pi))
result = gamma_fourth_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))