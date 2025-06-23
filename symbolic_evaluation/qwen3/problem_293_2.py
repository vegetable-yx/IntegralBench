import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^3
pi_cubed = mp.pi ** 3

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Calculate Gamma(3/4) and raise it to the 4th power
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_3_4_power = gamma_3_4 ** 4

# Calculate denominator: 8 * sqrt(2) * Gamma(3/4)^4
denominator = 8 * sqrt_two * gamma_3_4_power

# Compute final result
result = pi_cubed / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))