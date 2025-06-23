import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate π^(3/2)
pi_power = mp.power(mp.pi, 1.5)

# Calculate Γ(3/4)
gamma_val = mp.gamma(0.75)

# Square the gamma value
gamma_sq = gamma_val ** 2

# Calculate √2
sqrt2 = mp.sqrt(2)

# Compute denominator: √2 * [Γ(3/4)]^2
denominator = sqrt2 * gamma_sq

# Compute the final result: π^(3/2) / denominator
result = pi_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))