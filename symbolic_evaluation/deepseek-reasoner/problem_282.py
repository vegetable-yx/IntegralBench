import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_squared = gamma_1_4 ** 2

# Compute 2^(3/4)
denominator_2 = mp.power(2, mp.mpf(3)/4)

# Combine all components into the final result
result = (sqrt_pi * gamma_squared) / denominator_2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))