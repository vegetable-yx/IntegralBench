import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate 2^(3/4)
two_power = mp.power(2, mp.mpf(3)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Combine components for numerator and denominator
numerator = two_power * sqrt_pi * gamma_1_4
denominator = gamma_3_4

# Final result
result = numerator / denominator

print(mp.nstr(result, n=10))