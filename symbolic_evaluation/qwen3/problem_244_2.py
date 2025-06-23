import mpmath as mp
mp.dps = 15

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Raise Gamma(1/4) to the 8th power
gamma_power = gamma_1_4 ** 8

# Compute pi squared
pi_squared = mp.pi ** 2

# Calculate the denominator 24 * pi^2
denominator = 24 * pi_squared

# Compute final result by dividing gamma^8 by denominator
result = gamma_power / denominator

print(mp.nstr(result, n=10))