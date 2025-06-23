import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2^(3/2) = 2 * sqrt(2)
two_power_3_2 = 2 * mp.sqrt(2)

# Calculate sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate the modified Bessel function I_{3/4}(1/2)
bessel_val = mp.besseli(mp.mpf(3)/4, mp.mpf(1)/2)

# Combine all parts: (2^(3/2) * sqrt(pi) * Gamma(1/4) * bessel_val) / 20
result = (two_power_3_2 * sqrt_pi * gamma_1_4 * bessel_val) / 20

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))