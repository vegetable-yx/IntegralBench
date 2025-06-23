import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(1/4)^4
gamma_power = gamma_1_4**4

# Calculate denominator components
sqrt_2 = mp.sqrt(2)
denominator = 8 * sqrt_2 * mp.pi

# Final result
result = gamma_power / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))