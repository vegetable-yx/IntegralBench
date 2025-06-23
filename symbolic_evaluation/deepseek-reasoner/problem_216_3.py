import mpmath as mp
mp.dps = 15

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute 2^(1/4) using power function
two_power = mp.power(2, mp.mpf(1)/4)

# Calculate denominator: 2^(1/4) * Gamma(3/4)
denominator = two_power * gamma_3_4

# Calculate numerator: sqrt(pi) * Gamma(1/4)
numerator = sqrt_pi * gamma_1_4

# Final result calculation
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))