import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Combine the components: sqrt(pi) * Gamma(1/4) / Gamma(3/4)
result = sqrt_pi * gamma_1_4 / gamma_3_4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))