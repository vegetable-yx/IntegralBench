import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the constant pi
pi = mp.pi

# Calculate the square root of pi
sqrt_pi = mp.sqrt(pi)

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Calculate the ratio of Gamma(1/4) to Gamma(3/4)
gamma_ratio = gamma_1_4 / gamma_3_4

# Combine terms: 2 * pi * sqrt(pi) * (Gamma(1/4)/Gamma(3/4))
result = 2 * pi * sqrt_pi * gamma_ratio

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))