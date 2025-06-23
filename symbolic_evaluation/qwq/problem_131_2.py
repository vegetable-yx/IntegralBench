import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function value
gamma_squared = gamma_1_4 ** 2

# Calculate 2^(5/4)
two_power = mp.power(2, mp.mpf(5)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Combine denominator components
denominator = two_power * sqrt_pi

# Compute final result
result = gamma_squared / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))