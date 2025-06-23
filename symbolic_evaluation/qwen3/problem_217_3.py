import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma value
gamma_squared = gamma_1_4 ** 2

# Calculate 2^(1/4) using exact exponent
two_power = 2 ** (mp.mpf(1)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Combine denominator components
denominator = two_power * sqrt_pi

# Compute final result
result = gamma_squared / denominator

# Print with 10 decimal precision
print(mp.nstr(result, n=10))