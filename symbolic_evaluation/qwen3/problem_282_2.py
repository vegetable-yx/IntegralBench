import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate 2^(3/2)
two_power = mp.power(2, mp.mpf(3)/2)

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) term
gamma_squared = mp.power(gamma_1_4, 2)

# Calculate numerator: 2^(3/2) * Gamma(1/4)^2
numerator = two_power * gamma_squared

# Calculate denominator: sqrt(pi)
denominator = mp.sqrt(mp.pi)

# Final result
result = numerator / denominator

print(mp.nstr(result, n=10))