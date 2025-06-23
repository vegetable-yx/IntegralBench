import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute the fourth power of Gamma(1/4)
gamma_power = gamma_1_4**4

# Calculate the denominator 8π
denominator = 8 * mp.pi

# Compute the final result
result = gamma_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))