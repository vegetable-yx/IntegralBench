import mpmath as mp
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function value
gamma_squared = gamma_1_4 ** 2

# Calculate sqrt(2π)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Compute final result by multiplying components
result = sqrt_2pi * gamma_squared

print(mp.nstr(result, n=10))